
from django.db import models
from User.models import User
class deposite_request(models.Model):
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Deposite Request'
        verbose_name_plural = 'Deposite Request'
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    admin_account = models.CharField(  verbose_name="Admin account" ,max_length=50)
    amount = models.CharField(max_length=50)
    customer_name = models.CharField( verbose_name="Customer Bank Name" ,max_length=50)
    transaction_id = models.CharField(max_length=50)
    is_deposited = models.BooleanField(default=False)
    request_at = models.DateTimeField(auto_now_add=True)
    is_accpted = models.BooleanField(default=False)
    def __str__(self):
        return self.username.username

class transaction(models.Model):
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Deposit and withdrawl'
        verbose_name_plural = 'Deposit and withdrawl'
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    deposite_amount = models.CharField(verbose_name=("total deposite amount"),default=0.0 , max_length=50)
    widthdrawl_amount = models.CharField(verbose_name=("total withdrawl amount") ,default=0.0 , max_length=50)
    
    
class withdraw_request(models.Model):
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Withdrawal request'
        verbose_name_plural = 'Withdrawal request'
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    method = models.CharField(max_length=50)
    type= models.CharField(max_length=50)
    amount = models.CharField(max_length=50)
    account_holder = models.CharField( verbose_name="Account Holder Number" ,max_length=50)
    is_withdrawl = models.BooleanField(default=False)
    is_accpted = models.BooleanField(default=False)
    request_at = models.DateTimeField(auto_now_add=True)
