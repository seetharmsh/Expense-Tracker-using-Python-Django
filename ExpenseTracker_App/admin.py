from django.contrib import admin
from ExpenseTracker_App.models import UserBalanceModel,TransactionModel



# Register your models here.
admin.site.register(UserBalanceModel)
admin.site.register(TransactionModel)