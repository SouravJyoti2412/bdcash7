import json
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from User.models import User
from Website_Setting.models import Homepage_animated_line, website_logo
from django.views.decorators.csrf import csrf_exempt
from all_payments.models import deposite_request ,transaction, withdraw_request
from django.contrib import messages
# from django.utils import


def home(request):
    user = request.user
    if request.user.is_anonymous:
        deposite_amount =0.0
    else:
        
        deposite = transaction.objects.get(username= user)
        deposite_amount =deposite.deposite_amount
    context={
    'marquree' : Homepage_animated_line.objects.all(),
    'logo': website_logo.objects.all(),
    'deposite_amount' : deposite_amount
    }
    
    return render(request,"index.html",context)

@csrf_exempt
def deposite_money(request):
    if request.method == "POST":
        user = request.user
        to_admin = request.POST["to"]
        amount = request.POST["amount"]
        from_user = request.POST["from"]
        transection_id= request.POST["transection_number"]
        print(user,to_admin,amount,from_user,transection_id)
        deposite = deposite_request(username=user,
                                    admin_account =to_admin,
                                    amount = amount,
                                    customer_name = from_user,
                                    transaction_id =transection_id)
        deposite.save()
        data = {'amount':amount, "result":" rupess deposite request sucessfully send to admin"}
        return JsonResponse(data)

    else:
        return render(request,"404.html")
    
    
    
def widthdrawl_request(request):
    
    if request.method=="POST":
        user = request.user
        deposite_amount=transaction.objects.get(username = user)
        payment_method = request.POST["withdraw_method"]
        type = request.POST["account_type"]
        amount = request.POST["withdraw_amount"]
        user_acc_number = request.POST["withdraw_to"]
        if float(amount) > float(deposite_amount.deposite_amount):
            messages.error(request,"insufficiant balance", extra_tags="singup_error")
            return redirect("/wallet")
        if int(amount) >= 500 and int(amount) <= 25000 :
            widthdrawl_data = withdraw_request(username=user,
                                           method=payment_method,
                                           type=type,
                                           amount=amount,
                                           account_holder=user_acc_number)
            widthdrawl_data.save()
            messages.success(request,"Your widthdraw request send sucessfully",extra_tags="singup_success")
            return redirect("/wallet")
        else:
            messages.error(request,"minimum witdrawl value 500 tk and max amount 25000 tk", extra_tags="singup_error")
            return redirect("/wallet")
    else:
        return render(request,"404.html")
        
    
    


def wallet(request):
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
    'user':User.objects.get(username=user)
    }
    
    return render(request, "index1.html",context)