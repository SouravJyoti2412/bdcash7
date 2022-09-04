from django.contrib import messages
from django.shortcuts import render,redirect
# from rest_framework.views import  APIView
# from rest_framework.permissions import IsAuthenticated
from all_payments.models import transaction, deposite_request, withdraw_request
from django.contrib.auth import authenticate, login
# class CategoryList(APIView):
#     permission_classes =[IsAuthenticated]
#     def post(self,request,format=None):


# def depsite_to_user(request,id):
    
#     data1 = deposite_request.objects.get(pk=id)
#     if data1.is_deposite == True :
#         deposite = transaction.objects.get(user = data1.user)
#         if request.method == "GET":
#             deposite.deposite_amount = data1.amount
#             deposite.save(update_fields=['deposite_amount'])
            
#     return redirect(request,'/admin/all_payments/transaction/')
            
def make_deposite(request,id ):
    data1 =deposite_request.objects.get(pk=id)
    user= data1.username
    if data1.is_accpted == True:
        if data1.is_deposited == True:
            messages.success(request,"your deposite already successfull", extra_tags="success")
            return redirect("/admin/all_payments/deposite_request/")
        else:    
            data1.is_deposited = True
            data1.save(update_fields=['is_deposited']) 
            money_deposite = transaction.objects.get(username =user )
            money_deposite.deposite_amount =float(money_deposite.deposite_amount) + float(data1.amount)
            money_deposite.save(update_fields=['deposite_amount'])
            messages.success(request,"your deposite amount added successfully")
    else:
        messages.error(request,"please first accept the request of deposite" , extra_tags="error")
    
    return redirect("/admin/all_payments/deposite_request/")        


        
    

def make_accept(request,id):
    
    data1 =deposite_request.objects.get(pk=id)
    data1.is_accpted = True
    data1.save(update_fields=['is_accpted']) 
    messages.success(request,"deposite request accept successfully")
    return redirect("/admin/all_payments/deposite_request/")







def make_widthdrawal(request,id ):
    data1 =withdraw_request.objects.get(pk=id)
    user= data1.username
    if data1.is_accpted == True:
        if data1.is_withdrawl == True:
            messages.success(request,"your widthdrawal already successfull", extra_tags="success")
            return redirect("/admin/all_payments/withdraw_request/")
        else:    
            data1.is_withdrawl = True
            data1.save(update_fields=['is_withdrawl']) 
            money_withdrawal = transaction.objects.get(username =user )
            print(money_withdrawal)
            print(data1.amount)
            print(money_withdrawal.widthdrawl_amount )
            money_withdrawal.deposite_amount =float(money_withdrawal.deposite_amount) - float(data1.amount)
            money_withdrawal.save(update_fields=['deposite_amount'])
            money_withdrawal.widthdrawl_amount = float(data1.amount)
            money_withdrawal.save(update_fields=['widthdrawl_amount'])
            messages.success(request,"your widthdrawal amount added successfully")
    else:
        messages.error(request,"please first accept the request of widthdrawal" , extra_tags="error")
    
    return redirect("/admin/all_payments/withdraw_request/")        
    

def accept(request,id):
    
    data1 =withdraw_request.objects.get(pk=id)
    data1.is_accpted = True
    data1.save(update_fields=['is_accpted']) 
    messages.success(request,"Widthdrawal request accept successfully")
    return redirect("/admin/all_payments/withdraw_request/")