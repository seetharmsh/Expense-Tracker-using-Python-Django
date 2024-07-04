from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_delete, pre_save
from django.dispatch import receiver
from .models import UserBalanceModel, TransactionModel

'''
@receiver(post_save,sender=User)
def create_user_balance(sender,instance,created,**kwargs):
    if created:
        UserBalanceModel.objects.create(user=instance,balance=0.00)
'''

'''
@receiver(pre_save, sender=TransactionModel)
def adjust_balance_on_edit(sender, instance, **kwargs):
    if instance.pk:
        old_instance = TransactionModel.objects.get(pk=instance.pk)
        balance = UserBalanceModel.objects.get(user=instance.user)

        # Reverse the effect of the old transaction
        if old_instance.transaction_type == 'deposit':
            balance.balance -= old_instance.amount
        elif old_instance.transaction_type == 'withdrawal':
            balance.balance += old_instance.amount

        # Apply the effect of the new transaction
        if instance.transaction_type == 'deposit':
            balance.balance += instance.amount
        elif instance.transaction_type == 'withdrawal':
            balance.balance -= instance.amount

        balance.save()
'''

'''
@receiver(post_save, sender=TransactionModel)
def update_balance_on_save(sender, instance, created, **kwargs):
    if created:
        balance, created = UserBalanceModel.objects.get_or_create(user=instance.user)
        if instance.transaction_type == 'deposit':
            balance.balance += instance.amount
        elif instance.transaction_type == 'withdrawal':
            balance.balance -= instance.amount
        balance.save()
'''

'''
@receiver(pre_delete,sender=TransactionModel)
def update_balance_on_delete(sender,instance,**kwargs):
    balance = UserBalanceModel.objects.get(user=instance.user)
    if instance.transaction_type == 'deposit':
        balance.balance -= instance.amount
    if instance.transaction_type == 'withdrawal':
        balance.balance += instance.amount
    balance.save()
'''