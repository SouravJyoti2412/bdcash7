from django.contrib import admin

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,User_game_statement

admin.site.register(User, UserAdmin)
admin.site.register(User_game_statement)
