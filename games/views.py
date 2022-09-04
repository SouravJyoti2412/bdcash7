import random
from re import S
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from User.models import User_game_statement
from Website_Setting.models import website_logo
from django.views.decorators.csrf import csrf_exempt
import random
from all_payments.models import transaction

@csrf_exempt
def game1(request):
    gamename="coin rotation"
    username = request.user
    coin = ["1","2"]
    result = ''
    toss_result =""
    stake=""
    deposite =0.0
    rate = 1.75
    toss = random.choice(coin)
    coin_stake=''
    
    if request.method =="POST":
        coin_stake = request.POST["coin_stake"]
        coin_amount = request.POST["coin_amount"]
        user = request.POST["user"]
        coin_amount = float(coin_amount)
        coin_win = coin_amount*0.75
        win_amount = coin_win+coin_amount
        # coin_pwin = request.POST["coin_pwin"]
        trans = transaction.objects.get(username = username)
        id = trans.id 
        deposite = trans.deposite_amount
        deposite= float(deposite)
        if coin_stake == "1":
            stake= "Head"
        else :
            stake="Tail"
        
        # print(coin_stake, coin_amount,trans)
        # # print(trans.deposite_amount)
        # print(toss)
        if deposite == 0.0 or deposite <=coin_amount:
            result ="you don't have sufficient money for playing the game"
        else:
            if coin_stake == toss:
                result = "you win !"
                data1 = transaction.objects.get(pk=id)
                data1.deposite_amount =  deposite + float(coin_win)
                data1.save(update_fields=['deposite_amount'])
                if toss == "1" :
                    toss_result = "HEAD"
                else:
                    toss_result = "TAIL"
            else:
                result ="you loose !"
                data1 = transaction.objects.get(pk=id)
                data1.deposite_amount =  deposite - coin_amount
                data1.save(update_fields=['deposite_amount'])
                if toss == "1" :
                    toss_result = "HEAD"
                else:
                    toss_result = "TAIL"
            game_statement = User_game_statement(user=username,
                                                game_name=gamename,
                                                stake = stake,
                                                Luck_stake = toss_result,
                                                Amount = coin_amount,
                                                Rate = rate,
                                                Return_Amount = win_amount,
                                                Win_Lose = result)
            game_statement.save()
        data= {
             'result':result ,
            # 'toss':toss,
            'toss_result':toss_result,
            'deposite':deposite
            
            # 'coin_value':coin_value
        }
        return JsonResponse(data)
    context ={
        'logo': website_logo.objects.all()
    }
    return render(request, "coin.html",context)

@csrf_exempt
def game2(request):
    gamename="ludo game"
    username = request.user
    coin = ["1","2","3","4","5","6"]
    result = ''
    toss_result =""
    error =""
    stake=""
    rate = 2
    deposite =0.0
    toss = random.choice(coin)
    if request.method =="POST":
        stake = request.POST["stake"]
        amount = request.POST["amount"]
        amount = float(amount)
        coin_win = amount*1
        win_amount = coin_win+amount
        # coin_pwin = request.POST["coin_pwin"]
        trans = transaction.objects.get(username = username)
        id = trans.id 
        deposite = trans.deposite_amount
        deposite= float(deposite)
        # print(coin_stake, coin_amount,trans)
        # # print(trans.deposite_amount)
        # print(toss)
        if deposite == 0.0 or deposite <=amount:
            error ="you don't have sufficient money for playing the game"
            
        else:
            if stake == toss:
                result = "you win !"
                data1 = transaction.objects.get(pk=id)
                data1.deposite_amount =  deposite + float(coin_win)
                data1.save(update_fields=['deposite_amount'])
                toss_result =  toss
            
            else:
                result ="you loose !"
                data1 = transaction.objects.get(pk=id)
                data1.deposite_amount =  deposite - amount
                data1.save(update_fields=['deposite_amount'])
                toss_result =  toss
        game_statement = User_game_statement(user=username,
                                                game_name=gamename,
                                                stake = stake,
                                                Luck_stake = toss_result,
                                                Amount = amount,
                                                Rate = rate,
                                                Return_Amount = win_amount,
                                                Win_Lose = result)
        game_statement.save()    
        data= {
             'result':result ,
            # 'toss':toss,
            'toss_result':toss_result,
            'deposite':deposite,
            'error': error
            
            # 'coin_value':coin_value
        }
        return JsonResponse(data)
   
    
    
    
    
    context ={
        'logo': website_logo.objects.all()
    }
    return render(request, "ludu.html",context)


@csrf_exempt
def game3(request):
    username = request.user
    coin = ["even","odd"]
    result = ''
    toss_result =""
    login_error =""
    error =""
    # coin_value =""
    rate = 1.80
    gamename ="ludo odd even"
    deposite =0.0
    stake=""
    toss = random.choice(coin)
    if request.method =="POST":
        stake = request.POST["stake"]
        amount = request.POST["amount"]
        amount = float(amount)
        coin_win = amount*0.8
        win_amount = coin_win+amount
        # coin_pwin = request.POST["coin_pwin"]
        trans = transaction.objects.get(username = username)
        id = trans.id 
        deposite = trans.deposite_amount
        deposite= float(deposite)
        # print(coin_stake, coin_amount,trans)
        # # print(trans.deposite_amount)
        # print(toss)
        if deposite == 0.0 or deposite <=amount:
            error ="you don't have sufficient money for playing the game"
            
        else:
            if stake == toss:
                result = "you win !"
                data1 = transaction.objects.get(pk=id)
                data1.deposite_amount =  deposite + float(coin_win)
                data1.save(update_fields=['deposite_amount'])
                toss_result =  toss
                
            else:
                result ="you loose !"
                data1 = transaction.objects.get(pk=id)
                data1.deposite_amount =  deposite - amount
                data1.save(update_fields=['deposite_amount'])
                toss_result =  toss
            game_statement = User_game_statement(user=username,
                                                game_name=gamename,
                                                stake = stake,
                                                Luck_stake = toss_result,
                                                Amount = amount,
                                                Rate = rate,
                                                Return_Amount = win_amount,
                                                Win_Lose = result)
            game_statement.save()     
        data= {
             'result':result ,
            'toss_result':toss_result,
            'deposite':deposite,
            'error': error
            
            # 'coin_value':coin_value
        }
        return JsonResponse(data)
    context ={
        'logo': website_logo.objects.all()
    }
    return render(request, "ludu-oe.html",context )
@csrf_exempt
def game4(request):
    gamename="Coin 3 in 1"
    username = request.user
    coin = ["1","2","3"]
    result = ''
    toss_result =""
    login_error =""
    error =""
    # coin_value =""
    rate = 1.85
    deposite =0.0
    stake=''
    toss = random.choice(coin)
    if request.method =="POST":
        stake = request.POST["stake"]
        amount = request.POST["amount"]
        amount = float(amount)
        coin_win = amount*0.85
        win_amount = coin_win+amount
        # coin_pwin = request.POST["coin_pwin"]
        trans = transaction.objects.get(username = username)
        id = trans.id 
        deposite = trans.deposite_amount
        deposite= float(deposite)
        # print(coin_stake, coin_amount,trans)
        # # print(trans.deposite_amount)
        # print(toss)
        if deposite == 0.0 or deposite <=amount:
            error ="you don't have sufficient money for playing the game"
            
        else:
            if stake == toss:
                result = "you win !"
                data1 = transaction.objects.get(pk=id)
                data1.deposite_amount =  deposite + float(coin_win)
                data1.save(update_fields=['deposite_amount'])
                toss_result =  toss
                
            else:
                result ="you loose !"
                data1 = transaction.objects.get(pk=id)
                data1.deposite_amount =  deposite - amount
                data1.save(update_fields=['deposite_amount'])
                toss_result =  toss
        game_statement = User_game_statement(user=username,
                                                game_name=gamename,
                                                stake = stake,
                                                Luck_stake = toss_result,
                                                Amount = amount,
                                                Rate = rate,
                                                Return_Amount = win_amount,
                                                Win_Lose = result)
        game_statement.save()          
        data= {
             'result':result ,
            'toss_result':toss_result,
            'deposite':deposite,
            'error': error
            
            # 'coin_value':coin_value
        }
        return JsonResponse(data)
    
    
    
    
    context ={
        'logo': website_logo.objects.all()
    }
    return render(request, "threeinone.html",context)




@csrf_exempt
def game5(request):
    username = request.user
    coin = ["1","2","3"]
    result = ''
    toss_result =""
    login_error =""
    error =""
    # coin_value =""
    gamename="3 In 1 Ball"
    rate ="1.80"
    stake=""
    deposite =0.0
    toss = random.choice(coin)
    if request.method =="POST":
        stake = request.POST["stake"]
        amount = request.POST["amount"]
        amount = float(amount)
        coin_win = amount*0.80
        win_amount = coin_win+amount
        # coin_pwin = request.POST["coin_pwin"]
        trans = transaction.objects.get(username = username)
        id = trans.id 
        deposite = trans.deposite_amount
        deposite= float(deposite)
        if stake == "1":
            stakes= "FOTBALL"
        elif stake=="2":
            stakes="CRICKET"
        else: 
            stakes ="TANIS"
        if deposite == 0.0 or deposite <=amount:
            error ="you don't have sufficient money for playing the game"
            
        else:
            if stake == toss:
                result = "you win !"
                data1 = transaction.objects.get(pk=id)
                data1.deposite_amount =  deposite + float(coin_win)
                data1.save(update_fields=['deposite_amount'])
                if toss == "1" :
                    toss_result = "FOOTBALL"
                    
                elif toss=="2":
                     toss_result = "CRICKET"
                else :
                    
                    toss_result = "TANNIS"
                
            else:
                result ="you loose !"
                data1 = transaction.objects.get(pk=id)
                data1.deposite_amount =  deposite - amount
                data1.save(update_fields=['deposite_amount'])
                if toss == "1" :
                    toss_result = "FOOTBALL"
                elif toss=="2":
                     toss_result = "CRICKET"
                else :
                    toss_result = "TANNIS"
            game_statement = User_game_statement(user=username,
                                                game_name=gamename,
                                                stake = stakes,
                                                Luck_stake = toss_result,
                                                Amount = amount,
                                                Rate = rate,
                                                Return_Amount = win_amount,
                                                Win_Lose = result)
            game_statement.save()      
        data= {
             'result':result ,
            'toss_result':toss_result,
            'deposite':deposite,
            'error': error
            
            # 'coin_value':coin_value
        }
        return JsonResponse(data)
    context ={
        'logo': website_logo.objects.all()
    }
    return render(request, "threeinoneball.html",context)




@csrf_exempt
def game6(request):
    
    username = request.user
    coin = ["1","2"]
    result = ''
    toss_result =""
    login_error =""
    error =""
    # coin_value =""
    deposite =0.0
    gamename ="one two"
    stake=''
    rate = 1.75
    toss = random.choice(coin)
    if request.method =="POST":
        stake = request.POST["stake"]
        amount = request.POST["amount"]
        amount = float(amount)
        coin_win = amount*0.75
        win_amount = coin_win+amount
        # coin_pwin = request.POST["coin_pwin"]
        trans = transaction.objects.get(username = username)
        id = trans.id 
        deposite = trans.deposite_amount
        deposite= float(deposite)
        # print(coin_stake, coin_amount,trans)
        # # print(trans.deposite_amount)
        # print(toss)
        if deposite == 0.0 or deposite <=amount:
            error ="you don't have sufficient money for playing the game"
            
        else:
            if stake == toss:
                result = "you win !"
                data1 = transaction.objects.get(pk=id)
                data1.deposite_amount =  deposite + float(coin_win)
                data1.save(update_fields=['deposite_amount'])
                toss_result =  toss
                
            else:
                result ="you loose !"
                data1 = transaction.objects.get(pk=id)
                data1.deposite_amount =  deposite - amount
                data1.save(update_fields=['deposite_amount'])
                toss_result =  toss
            game_statement = User_game_statement(user=username,
                                                game_name=gamename,
                                                stake = stake,
                                                Luck_stake = toss_result,
                                                Amount = amount,
                                                Rate = rate,
                                                Return_Amount = win_amount,
                                                Win_Lose = result)
            game_statement.save()     
        data= {
             'result':result ,
            'toss_result':toss_result,
            'deposite':deposite,
            'error': error
            
            # 'coin_value':coin_value
        }
        return JsonResponse(data)
    
    context ={
        'logo': website_logo.objects.all()
    }
    return render(request, "onetwo.html",context)