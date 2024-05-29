from ctypes.wintypes import MSG
import email
from turtle import update
from urllib import request
from django.contrib import messages
from datetime import date
from datetime import datetime
from random import randrange
from time import ctime, time
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from .models import *
from django.conf import settings
from django.core.mail import send_mail
from random import randrange
from .models import tbooking
from django.db.models import Q
from django.db.models import Sum
import time


# Create your views here.
def index(request):
    return render(request,'index2.html')

    

def booking(request):   
    if request.method=="POST":
        check1=request.POST['phone']
        request.session['check']=check1
        # print(request.session['check'])
        fname= request.POST['fname']
        lname= request.POST['lname']
        email= request.POST['email']
        # phone= request.POST['phone'],
        phone= request.POST['phone']
        capacity= request.POST['btable']
        bdate= request.POST['bdate']
        btime= request.POST['btime']
        
        global temp 
        cdate=Q(date=request.POST['bdate'])
        ctime=Q(time=request.POST['btime'])
        bookings = tbooking.objects.filter(cdate & ctime)
        if bookings.exists():
            print('this is the data you want')
            lastbookedtable = bookings.last().tno
            print(lastbookedtable)
            if lastbookedtable >=5:
                messages.info(request,'booking full')
                return render(request,'register-reservation.html')
            else:
                newbookedtable = lastbookedtable + 1
                firsttno = tableno.objects.get(tno=newbookedtable)
        else:
            newbookedtable=1
        temp={
            'fname':request.POST['fname'],
            'lname': request.POST['lname'],
            'email': request.POST['email'],
            # phone= request.POST['phone'],
            'phone': request.POST['phone'],
            'capacity': request.POST['btable'],
            'date': request.POST['bdate'],
            'time': request.POST['btime'],
            'tno':newbookedtable
        }
        otp=randrange(1000,9000)
        subject = 'welcome to Apna Restaurant'
        message = f'Hello {fname}!! Your otp is {otp}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail( subject, message, email_from, recipient_list )
        return render(request,'otp.html',{'otp' : otp})
    else:
        msg="booking is not available at this time plz change date or time"
        return render(request,'register-reservation.html',{'msg' : msg})

        # return render(request,'otp.html',{'otp':otp})
        
        
        # try:
        #     # cdate=Q(date=bdate)
        #     # ctime=Q(time=btime)
        #     # bookings = tbooking.objects.filter(cdate & ctime)
        #     # if booking.exists():
        #     #     # print(tbooking.objects.filter(tableno.tno))\
        #     #     for bkngs in bookings:
        #     #         print(bkngs.Tableno.tno)
                

        #         pass
        #     else:
        #         pass
            
        # except:
        #     pass

        # try:
        #     if(tbooking.objects.get(date=request.POST['bdate']).exists()):
        #         pass
        #     else:
        #         pass
            
        # except:
        #     pass
        
        # if(
            
        # ):
        #     pass
        # else:
        #     pass

        # booking = tbooking(fname=fname,lname = lname,email=email,phone=phone,capacity=capacity,date=bdate,time=btime)
        # booking.save()


      


    
def otp(request):
    if request.method=="POST" :
        global temp
        otp=request.POST.get('otp')
        uotp=request.POST.get('uotp')
        print(otp)
        print(uotp)
        print(request.session['check'])
        
        if(otp==uotp):
            
            if tbooking.objects.filter(phone=request.session['check']).exists():
                datetimecheck=check.objects.create(cdate=temp['date'],ctime=temp['time'])
                udate=datetimecheck.cdate
                utime=datetimecheck.ctime
                # print(udate)
                # d1=time.strptime(udate, "%Y-%m-%d")
                # print(d1)
                # timestampStr1 = cdate.strftime("%d %b %Y ") 2022-03-30
                print("ok")
                available1=tbooking.objects.get(phone=request.session['check'])
                cdate=available1.date
                ctime=available1.time
                cstatus=available1.rstatus
                print(cstatus)
                # d2=cdate-d1

                # print(d2)
                # print(utime)
                # print(type(utime))
                
                timestampStr = cdate.strftime("%Y-%m-%d")
                timestampStr1=ctime.strftime("%H:%M:%S")
                print(timestampStr1)
                print(type(timestampStr1))
                # print(type(timestampStr))
                # ft=date(udate)
                # timestampStr1 = udate.strftime("%d %b %Y ")
                # print(ft)
                # print(timestampStr1)
                # timestampStr==udate
                # print(timestampStr)
                # print(udate)
                # if  (timestampStr!=udate):
                #     if(cstatus=="None"):
                #         msg='Plz try after some time'
                #         subject = 'welcome to Apna Restaurant'
                #         message = f'Hello {available1.fname}!! Your  booking status is pending because your  !! booking time: {available.date} !! booking time: {available.time}'
                #         email_from = settings.EMAIL_HOST_USER
                #         recipient_list = [available.email, ]
                #         send_mail( subject, message, email_from, recipient_list )

                if  (timestampStr==udate):
                    if(timestampStr1==utime):
                       msg="Already has today's booking"
                    else: 
                        available=tbooking.objects.get(phone=request.session['check'])
                        print(available.fname)
                        print(temp['lname'])
                    
                        available.fname= temp['fname']
                        available.lname= temp['lname']
                        available.email= temp['email']
                        
                        available.capacity= temp['capacity']
                        available.date= temp['date']
                        available.time= temp['time']
                        available.tno=temp['tno']
                        available.save()
                        msg='booking status updated'
                        subject = 'welcome to Apna Restaurant'
                        message = f'Hello {available.fname}!! Your  booking status is updated !! booking time: {available.date} !! booking time: {available.time}'
                        email_from = settings.EMAIL_HOST_USER
                        recipient_list = [available.email, ]
                        send_mail( subject, message, email_from, recipient_list )
                    
                else:
                    available=tbooking.objects.get(phone=request.session['check'])
                    print(available.fname)
                    print(temp['lname'])
                
                    available.fname= temp['fname']
                    available.lname= temp['lname']
                    available.email= temp['email']
                    
                    available.capacity= temp['capacity']
                    available.date= temp['date']
                    available.time= temp['time']
                    available.tno=temp['tno']
                    available.save()
                    msg='Thanks for Booking'
                    subject = 'welcome to Apna Restaurant'
                    message = f'Hello {available.fname}!! Your booking is Done !! booking time: {available.date}!! booking time: {available.time}'
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = [available.email, ]
                    send_mail( subject, message, email_from, recipient_list )
            else:
                # print("sinchen")
                tbooking.objects.create(
                    fname= temp['fname'],
                    lname= temp['lname'],
                    email= temp['email'],
                    phone= temp['phone'],
                    capacity= temp['capacity'],
                    date= temp['date'],
                    time= temp['time'],
                    tno=temp['tno'],
                )
                msg='Thanks for Booking'

                subject = 'welcome to Apna Restaurant'
                message = f'Hello {available.fname}!! Your booking is Done !! booking time: {available.date}!! booking time: {available.time}'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [available.email, ]
                send_mail( subject, message, email_from, recipient_list )
            del temp
            
            return render(request,'index2.html', {'msg' : msg})
        else:
            msg='otp is incorrect plz enter correct otp'
            return render(request,'otp.html',{'msg' : msg, 'otp' : otp})
    else :
        print("nahi ja raha")
        return render(request,otp.html)

def login(request): 

    try:
        request.session['user']
        msg='welcome back'
        
        return redirect('dashboard')
    except:
        if request.method=="POST":
            user=request.POST['user']
        
            if tbooking.objects.filter(phone=user).exists():
                request.session['user']=user
                msg='login success'
                cust=tbooking.objects.get(phone=user)
                trans_insert=clogin(cust_id=cust)
                trans_insert.save()
                
                request.session['transid']=trans_insert.trans_id
                print('/////////id')
                print(request.session['transid'])
                return redirect('dashboard')
                # return render(request,'dashboard.html', {'msg' : msg, 'uid' : uid })
            else:
                msg='Login fail'
                return render(request,'login.html', {'msg' : msg})
        else:
            return render(request,'login.html')

def dashboard(request):

    if 'user' not in request.session:
        return redirect('login')
    else:

        user=request.session['user']
        uid=tbooking.objects.get(phone=user)
        if request.method=="POST":

            uid.fname=request.POST.get('fname')
            uid.lname=request.POST.get('lname')
            uid.email=request.POST.get('email')
            uid.phone=request.POST.get('phone')
            uid.save()
            if request.FILES:
                uid.pic=request.FILES['pic']
                uid.save()
        allmenue=menu.objects.all()
        # print(uid.fname)
        # print(uid.lname)
        return render(request,'dashboard.html',{'uid' :uid,'menu' :allmenue})

def menue(request):
    if 'user' not in request.session:
        return redirect('login')
    else:

        user=request.session['user']
        cname=category.objects.all()
        # mlist=category.objects.all()
        mlist=menu.objects.all()
        data=[]
        categorylist=category.objects.all()
        for cat in categorylist:
            item=menu.objects.filter(item_category=cat)
            data.append(item)
    
        return render(request,'menu.html',{'cname':cname,'mlist':mlist,'data':data,'user':user})

def cart(request):
    return render(request,'index.html')

def order(request):
    return render(request,'order.html')

def logout(request):
    if 'user' not in request.session:
        return redirect('login')
    else:
        del request.session['user']
        return render(request,'login.html')


def checkout(request):
    if 'user' not in request.session:
        return redirect('login')
    else:
        

        #check something
        myorderr=customercart.objects.filter(ctrans_id=request.session['transid'])
        # <QuerySet [<customercart: 132>, <customercart: 133>, <customercart: 134>, <customercart: 135>, <customercart: 136>]>
        print('++++++++++++')
        c=myorderr.count()
        print(c)
        print(myorderr)
        for i in myorderr:
            orderid=i.ctrans_id.trans_id
            order_insert=myorder(order_id=orderid,order_item=i.item_id,cust_number=i.cust_number.phone,item_quantity=i.item_quantity,totalPrice=i.totalPrice,cust_details=i.cust_number)
            order_insert.save()
            print("ok janu")
            print(i.cust_number.fname)
        customercart.objects.filter(ctrans_id=request.session['transid']).delete()
        orderdet=myorder.objects.filter(order_id=request.session['transid'])
        # orderdet=orderdet.order_by('id').reverse()
        sum=0
        for i in orderdet:
            sum=sum+i.totalPrice
        print(sum)

        flag=1
        flag1=1
        for i in orderdet:
            if i.process_status!="delever":
                flag=0
        print(flag)

        # orderbill=orderdet.totalPrice.aggregate(sum('totalPrice'))
        return render(request,'checkout.html',{'order':orderdet,'total':sum,'flag':flag,'flag1':flag1})
        

def checkout1(request):
    # myorderr=customercart.objects.filter(ctrans_id=request.session['transid'])
    # for i in myorderr:
    
    print("session")
    print(request.session['user'])
    available=tbooking.objects.get(phone=request.session['user'])
    orderdet=myorder.objects.filter(order_id=request.session['transid'])
    sum=0
    for i in orderdet:
        sum=sum+i.totalPrice
    print("oyehoye")
    
    # checkt=transaction.objects.get(trans_id=request.session['transid'])
    value=request.session['transid']
    insertTransaction=transaction.objects.create(trans_id=request.session['transid'],total_price=sum)
    # del request.session['user']
    # del request.session['transid']
    return render(request,'invoicedetail.html',{'order':orderdet,'cust':available,'total':sum,'idd':value,'bill':insertTransaction})

# AJAX functions:/

def addtocartajax(request):
    userid=request.session['user']
    print('/////////////////////////////')
    
    productid = request.GET['productid']
    item = menu.objects.get(id=productid)
    print(item)
    # userphone = request['user']
    userphone = request.session['user']
    getuser = tbooking.objects.get(phone=userphone)
    print(getuser)
    print('asdasda')
    # userid=
    custcart = customercart.objects.filter(item_id = item , cust_number=getuser)
    if(custcart.exists()):
        cart = customercart.objects.get(item_id = item , cust_number=getuser)
        print('cart...................')

        print(cart.item_quantity)

        cart.item_quantity += 1
        cart.save()
    else:
        print('////////////id in ajax')
        print(request.session['transid'])

        transId = clogin.objects.get(trans_id=int(request.session['transid']))
        custcart = customercart(item_id = item , cust_number=getuser,ctrans_id=transId)
        custcart.save()
    allcart = customercart.objects.filter(cust_number=getuser)
    data =[]
    if allcart.exists():
        for items in allcart:

            productImage = str(items.item_id.pic)
            productName =str(items.item_id.item_name)
            productPrice =items.item_id.item_price
            totalPrice = items.totalPrice
            productId =str(items.item_id.id)
            print('/////////////////////////// items in views')
            print(productName)
            item = {
                'totalPrice' :  totalPrice,
                'productImage' :productImage,
                'productName' :productName,
                'productPrice' :productPrice,
                'productId' : productId,
            }
            data.append(item)
    print(data)
    return JsonResponse({'data':data})

def deletefromcartajax(request):
    print('///////////////////////////// user id:')
    userid=request.session['user']
    print(userid)
    productid = request.GET['productid']
    getcustomer = tbooking.objects.get(phone=userid)
    item = customercart.objects.filter(item_id=productid,cust_number=getcustomer).delete()

    userphone = 9016728455
    getuser = tbooking.objects.get(phone=userphone)
    allcart = customercart.objects.filter(cust_number=getuser)
    data =[]
    if allcart.exists():
        for items in allcart:
            productImage = str(items.item_id.pic)
            productName =str(items.item_id.item_name)
            productPrice =str(items.item_id.item_price)
            productId =str(items.item_id.id)
            print('/////////////////////////// items in views')
            print(productName)
            item = {  
                'productImage' :productImage,
                'status':'True',  
                'productName' :productName,
                'productPrice' :productPrice,
                'productId' : productId,
            }
    else:
        item={
            'status':'False'
        }
        data.append(item)
    return JsonResponse({'data':data})