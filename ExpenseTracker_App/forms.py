from django import forms
from django.contrib.auth.models import User
from ExpenseTracker_App.models import TransactionModel, UserBalanceModel

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name","last_name","email","username","password"]
        widgets = {
                    'first_name':forms.TextInput(attrs={'class':'form-control'}),
                    'last_name':forms.TextInput(attrs={'class':'form-control'}),
                    'email':forms.EmailInput(attrs={'class':'form-control'}),
                    'username':forms.TextInput(attrs={'class':'form-control'}),
                    'password':forms.PasswordInput(attrs={'class':'form-control'})
        }
        help_texts = {
            'username': None,
            'email': None,
        }

class LogInForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username","password"]
        widgets = {
                    'username':forms.TextInput(attrs={'class':'form-control'}),
                    'password':forms.PasswordInput(attrs={'class':'form-control'})
        }
        help_texts = {
            'username': None,
            'password': None,
        }

class AddTransactionForm(forms.ModelForm):
    class Meta:
        model = TransactionModel
        fields = ["transaction_name","transaction_type","amount"]
        widgets = {
                    'transaction_name':forms.TextInput(attrs={'class':'form-control'}),
                    'transaction_type':forms.Select(attrs={'class':'form-control'}),
                    'amount':forms.NumberInput(attrs={'class':'form-control'}),
        }


