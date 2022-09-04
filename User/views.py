
from enum import unique
from django.shortcuts import HttpResponse
from urllib import request
from django.shortcuts import render,redirect

from Website_Setting.models import Homepage_animated_line, website_logo
from .models import User,User_game_statement
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout
from all_payments.models import deposite_request, transaction, withdraw_request
# from django.contrib.auth.models import User 
def singup(request):
    if request.method =="POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        number = request.POST["number"]
        password = request.POST["password"]
        cpassword = request.POST["confirm_password"]
        # print(first_name,last_name,username ,email,number,password,cpassword)
        if User.objects.filter(username = username ) :
            messages.error(request,"your username must be unique", extra_tags="singup_error")
            return redirect("/")
        # if not username.isalnum():
        #     messages.error(request,"your username must be contain letter and number", extra_tags="singup_error")
        #     return redirect("/")
        if User.objects.filter(email = email):
            messages.error(request,"your email id already exist", extra_tags="singup_error")
            return redirect("/")
        
        all_user = User.objects.create_user(username,email,password)
        all_user.first_name = first_name
        all_user.last_name = last_name
        all_user.phoneno = number
        all_user.save()
        if request.method =="POST":
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(username = username , password = password)
            if user is not None:
                login(request, user)
                tran = transaction(username= user)
                tran.save()
        messages.success(request,"you account create sucessfully",extra_tags="singup_success")
        return redirect("/")
    else:
        return render(request, "404.html")
    
    
    
def handlelogin(request):
    if request.method =="POST":
        username = request.POST["user_name"]
        password = request.POST["password"]
        user = authenticate(username = username , password = password)
        if user is not None:
            login(request, user)
            
            messages.success(request,"you are login sucessfully",extra_tags="singup_success")
            return redirect("/")
        else:
            messages.error(request,"Invalid credential", extra_tags="singup_error")
            return redirect("/")
    return render(request, "404.html")    
def handlelogout(request):
    
    logout(request)
    messages.success(request,"you are loggout successfully",extra_tags="singup_success")
    return redirect("/")
    # return HttpResponse("handale_logout")
    
    #login user password change
def password_change(request):
    if request.method =="POST":
        loginuser =request.user 
        password = request.POST["current_password"]
        new_pass = request.POST["new_password"]
        con_new_pass = request.POST["confirm_password"]
        if password == new_pass:
            messages.error(request,"current password and new password same", extra_tags="singup_error")
            return redirect("/wallet")
        if new_pass != con_new_pass:
             messages.error(request,"new password and confirm new password not matched", extra_tags="singup_error")
             return redirect("/wallet")
        else:
            user = authenticate(username = loginuser , password = password)
            userid = User.objects.get(username = loginuser)
            id = userid.id 
            if user is not None:
                data1 = User.objects.get(pk=id)
                # data1.password =  new_pass
                print(data1.password)
                data1.set_password(new_pass)
                data1.save()
                # data1.save(update_fields=['password'])
                messages.success(request,"your password update successfully",extra_tags="singup_success")
                return redirect("/")
            else:
                messages.error(request,"you enter wrong current password", extra_tags="singup_error")
        return redirect("/wallet")         
    else:
        return render(request, "404.html")  
    
    
def user_statement(request):
    user = request.user
    if request.user.is_anonymous:
        deposite_amount =0.0
        return render(request, "404.html")   
    else:
        
        deposite = transaction.objects.get(username= user)
        deposite_amount =deposite.deposite_amount
        
        
    
    context={
    'marquree' : Homepage_animated_line.objects.all(),
    'logo': website_logo.objects.all(),
    'deposite_amount' : deposite_amount,
    'user':User.objects.get(username=user),
    'game_statement':User_game_statement.objects.filter(user = user).order_by('-id'),
    'deposite_statement':deposite_request.objects.filter(username = user).order_by('-id'),
    'widthdrawal_statement':withdraw_request.objects.filter(username = user).order_by('-id')
    }
    
    return render(request, 'user_statement.html',context)