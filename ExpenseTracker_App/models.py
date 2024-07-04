from django.db import models
from django.contrib.auth.models import User

class UserBalanceModel(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)

class TransactionModel(models.Model):
    TRANSACTION_TYPE_CHOICES = [('deposit','Deposit'),('withdrawal','Withdrawal',)]

    transaction_name = models.CharField(max_length=100)
    transaction_type = models.CharField(max_length=10,choices=TRANSACTION_TYPE_CHOICES)
    amount = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
