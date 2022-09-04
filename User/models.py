from django.db import models
from django.contrib.auth.models import AbstractUser
# from phonenumber_field.modelfields import PhoneNumberField

class User(AbstractUser):
     phoneno = models.CharField(max_length=10)
class User_game_statement(models.Model):
     class Meta:
          db_table = ''
          managed = True
          verbose_name = 'All user game statement'
          verbose_name_plural = 'All user game statement'
     user = models.ForeignKey(User,on_delete= models.CASCADE)     
     game_name = models.CharField(max_length=50)
     playing_time = models.DateTimeField(auto_now_add=True)
     stake =  models.CharField(max_length=50)
     Luck_stake = models.CharField(max_length=50)
     Amount = models.CharField(max_length=50)
     Rate = models.CharField(max_length=50)
     Return_Amount = models.FloatField()
     Win_Lose = models.CharField(max_length=50)
          
     
     