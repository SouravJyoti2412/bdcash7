from email import message
from django.contrib import admin
from all_payments.models import deposite_request,transaction, withdraw_request
from django.utils.html import format_html
class deposite_requestAdmin(admin.ModelAdmin):
    list_display = ('username','admin_account','amount','customer_name','transaction_id','request_at','is_deposited','is_accpted','deposite','Request_Accept')

    # def action(request,id):
    #     if 'is_deposited' is True:
    #         if request.method == 'POST':
    #             data1 = transaction.objects.get(pk=id)
    #             data1.deposite_amount = False 
    #             data1.save(update_fields=['active'])
    # def action(self, obj):
    #     return format_html(f'<button style="background-color:green;"><a href="/admin/Website_Setting/website_logo/{obj.id}/change/" class="default"style ="color:white;">edit</a></button>')     
    # actions =['make_deposite','deposite_accepted']
    
    
    def deposite(self,obj):
        return format_html(f'<button class="btn btn-info"><a href="/make_deposite/{obj.id}">deposite</a></button>')
    def Request_Accept(self,obj):
        return format_html(f'<button class="btn btn-success"><a href="/make_accept/{obj.id}" >Accept</a></button>')
    # def make_deposite(self,request,queryset):
    #     print(deposite_request.amount)
    #     # if self.deposite_request.is_accpted != True:
    #     #    self.message_user(request, "please first accepet the request")
    #     # else:
    #     queryset.update(is_deposited =True)
    # def deposite_accepted(self,request,queryset):
    #     queryset.update(is_accpted =True)
        # deposite = transaction.objects.filter(username =username)
        # deposite.deposite_amount = self.amount
        # deposite.save(update_fields=['deposite_amount'])
admin.site.register(deposite_request,deposite_requestAdmin)



class transactionAdmin(admin.ModelAdmin):
    list_display = ('username','deposite_amount','widthdrawl_amount')
    search_fields = ('username__username',)
admin.site.register(transaction, transactionAdmin)



class withdrawl_requestAdmin(admin.ModelAdmin):
    list_display =('username','method','type','amount','account_holder','request_at','is_withdrawl','is_accpted','witdrawal','Request_Accept')
    search_fields = ('username__username',)
    def witdrawal(self,obj):
        return format_html(f'<button class="btn btn-info"><a href="/make_widthdrawal/{obj.id}">deposite</a></button>')
    def Request_Accept(self,obj):
        return format_html(f'<button class="btn btn-success"><a href="/accept/{obj.id}" >Accept</a></button>')
admin.site.register(withdraw_request,withdrawl_requestAdmin)



