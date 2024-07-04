from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from ExpenseTracker_App.forms import SignUpForm, LogInForm, AddTransactionForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from ExpenseTracker_App.models import TransactionModel, UserBalanceModel
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
from django.core.mail import send_mail, settings

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'

'''
# Use when signls.py is given 
class SignUpView(View):

    def get(self,request,*args,**kwargs):
        form = SignUpForm()
        return render(request,'signup.html',{'formkey':form})
    
    def post(self,request,*args,**kwargs):
        data = SignUpForm(request.POST)
        if data.is_valid():
            User.objects.create_user(**data.cleaned_data)
            return redirect('LogIn')
        else:
            return HttpResponse("Invalid credentials")
'''

class SignUpView(View):

    def get(self,request,*args,**kwargs):
        form = SignUpForm()
        return render(request,'signup.html',{'formkey':form})
    
    def post(self,request,*args,**kwargs):
        data = SignUpForm(request.POST)
        if data.is_valid():
            user = User.objects.create_user(**data.cleaned_data)
            UserBalanceModel.objects.create(user=user,balance=0.00)
            send_mail('Welcome | PennyWise','Welcome, You have successfully created an account on PennyWise',settings.EMAIL_HOST_USER,[data.cleaned_data.get('email')])
            return redirect('LogIn')
        else:
            return HttpResponse("Invalid credentials")

class LogInView(View):

    def get(self,request,*args,**kwargs):
        form = LogInForm(request.POST)
        return render(request,'login.html',{'formkey':form})
    
    def post(self,request,*args,**kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('UserHome')
        else:
            messages.error(request,'Invalid Credentials')
            return redirect('LogIn')

class UserHomeView(TemplateView):
    template_name = 'userhome.html'

class LogOutView(View):

    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect('Home')
    
class ProfileView(View):
    
    def get(self,request,*args,**kwargs):
        data = User.objects.filter(username=request.user)
        return render(request,'profile.html',{'datakey':data})

'''
# Use when signls.py is given 
class AddTransactionView(View):

    def get(self,request,*args,**kwargs):
        form = AddTransactionForm
        return render(request,'addtransaction.html',{'formkey':form})
    
    def post(self,request,*args,**kwargs):
        data = AddTransactionForm(request.POST)
        if data.is_valid():
            data.instance.user = request.user
            data.save()
            return redirect('UserHome')
'''

class AddTransactionView(View):

    def get(self,request,*args,**kwargs):
        form = AddTransactionForm
        return render(request,'addtransaction.html',{'formkey':form})
    
    def post(self,request,*args,**kwargs):
        data = AddTransactionForm(request.POST)
        balance = UserBalanceModel.objects.get(user=request.user)
        if data.is_valid():
            data.instance.user = request.user

            if data.cleaned_data.get('transaction_type') == 'deposit':
                balance.balance += data.cleaned_data.get('amount')
            elif data.cleaned_data.get('transaction_type') == 'withdrawal':
                balance.balance -= data.cleaned_data.get('amount')

            balance.save()
            data.save()
            return redirect('ViewTransaction')
        
class ViewTransactionView(View):

    def get(self,request,*args,**kwargs):
        data = TransactionModel.objects.filter(user=request.user)
        return render(request,'viewtransactions.html',{'datakey':data})
    
class BalanceView(View):

    def get(self,request,*args,**kwargs):
        data = UserBalanceModel.objects.filter(user=request.user)
        return render(request,'viewbalance.html',{'datakey':data})

'''
# Use when signls.py is given 
class EditTransactionView(UpdateView):
    model = TransactionModel
    form_class = AddTransactionForm
    template_name = 'edittransaction.html'
    success_url = reverse_lazy('ViewTransaction')
    pk_url_kwarg = 'id'
'''

class EditTransactionView(View):

    def get(self,request,*args,**kwargs):
        id = kwargs.get('id')
        transaction = TransactionModel.objects.get(id=id)
        form = AddTransactionForm(instance=transaction)
        return render(request,'edittransaction.html',{'form':form})

    def post(self,request,*args,**kwargs):
        transaction_id = kwargs.get('id')
        old_data = TransactionModel.objects.get(id=transaction_id)
        balance = UserBalanceModel.objects.get(user=request.user)
        data = AddTransactionForm(request.POST,instance=old_data)

        # Reverse the effect of the old transaction
        if old_data.transaction_type == 'deposit':
            balance.balance -= old_data.amount
        elif old_data.transaction_type == 'withdrawal':
            balance.balance += old_data.amount

        if data.is_valid():
            # Apply the effect of the new transaction
            if data.cleaned_data.get('transaction_type') == 'deposit':
                balance.balance += data.cleaned_data.get('amount')
            elif data.cleaned_data.get('transaction_type') == 'withdrawal':
                balance.balance -= data.cleaned_data.get('amount')

            balance.save()
            data.save()
        
        return redirect('ViewTransaction')

'''
# Use when signls.py is given 
class DeleteTransactionView(View):
        def get(self,request,*args,**kwargs):
            transaction_id = kwargs.get('id')
            transaction = TransactionModel.objects.get(id=transaction_id)
            transaction.delete()
            return redirect('ViewTransaction')
'''

class DeleteTransactionView(View):
        def get(self,request,*args,**kwargs):
            transaction_id = kwargs.get('id')
            transaction = TransactionModel.objects.get(id=transaction_id)
            balance = UserBalanceModel.objects.get(user=request.user)
            if transaction.transaction_type == 'deposit':
                balance.balance -= transaction.amount
            if transaction.transaction_type == 'withdrawal':
                balance.balance += transaction.amount
            balance.save()
            transaction.delete()
            return redirect('ViewTransaction')