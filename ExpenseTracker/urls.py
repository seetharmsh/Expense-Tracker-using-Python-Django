"""
URL configuration for ExpenseTracker_Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ExpenseTracker_App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomeView.as_view(),name='Home'),
    path('SignUp',views.SignUpView.as_view(),name='SignUp'),
    path('LogIn',views.LogInView.as_view(),name='LogIn'),
    path('UserHome',views.UserHomeView.as_view(),name='UserHome'),
    path('LogOut',views.LogOutView.as_view(),name='LogOut'),
    path('Profile',views.ProfileView.as_view(),name='Profile'),
    path('AddTransaction',views.AddTransactionView.as_view(),name='AddTransaction'),
    path('ViewTransaction',views.ViewTransactionView.as_view(),name='ViewTransaction'),
    path('ViewBalance',views.BalanceView.as_view(),name='ViewBalance'),
    path('EditTransaction/<int:id>',views.EditTransactionView.as_view(),name='EditTransaction'),
    path('DeleteTransaction/<int:id>',views.DeleteTransactionView.as_view(),name='DeleteTransaction'),
]
