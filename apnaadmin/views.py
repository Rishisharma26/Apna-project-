from unicodedata import name

from django.shortcuts import render,redirect

# Create your views here.
from django.shortcuts import render

from myapp.models import category, menu, myorder, tbooking, yourorder
from .models import *
from django.db.models import Q

# Create your views here.
def aindex(request):
    return render(request,'index1.html')
    
def orders(request):
    
    order=myorder.objects.all()
    order=order.order_by('id').reverse()
    print(order)
    return render(request,'orders.html',{'order':order})

def status(request):
    
    if request.method=="POST":
        status=myorder.objects.get(id=request.POST['pk'])
        print('======================')
        print(request.POST['status'])
        status.process_status=request.POST['status']
        status.save()
        return redirect('orders')
    return render(request,'orders.html')

def rtable(request):
    # mlist=menu.objects.filter(item_name=cnamee)
    # getcat=category.objects.get(cname=cvalue)
    # getcid=category.objects.get(cname=cvalue)
    # mlist.itemcategory=getcat
    # mlist.itemcategory=getcid
    # print(cnamee)
    # mlist.save()    
    costumer=tbooking.objects.all().order_by('id').reverse()
    return render(request,'basic-tables.html',{'costumer':costumer,})

def mtable(request):
    if request.method=="POST":
        global cnamee
        cnamee=request.POST['name']
        global cvalue 
        cvalue=request.POST['category']
        menu.objects.create(
           # getcat=category.objects.get(cname=request.POST.get('category')),
            # getcid=category.objects.get(cname=request.POST.get('category'))
            item_name= request.POST['name'],
            item_price= request.POST['price'],
            item_desc= request.POST['desc'],
            # item_category=category.objects.create(cname=request.POST.get('categor y'),cid=request.POST.get('category')),
            # (cid=request.POST.get('category')),
            pic= request.FILES['pic'],
            availablity= request.POST['availabity'],   
        )
    menu_list=menu.objects.all()
    return render(request,'pages/product/productlist.html',{'menu':menu_list})

def medit(request,pk):
    menu_list=menu.objects.get(id=pk)
    costumer=category.objects.all()   
    if request.method=="POST":
        getcat=category.objects.get(cname=request.POST.get('category'))
        getcid=category.objects.get(cname=request.POST.get('category'))
        menu_liste=menu.objects.get(id=pk)
        menu_liste.item_name=request.POST.get('name')
        menu_liste.item_category=getcat
        menu_liste.item_category=getcid
        menu_liste.item_price=request.POST.get('price')
        menu_liste.item_desc=request.POST.get('desc')
        menu_liste.item_availabity=request.POST.get('availabity')
        menu_liste.save()
        if request.FILES:
            menu_liste.pic=request.FILES['pic']
            menu_liste.save()
        menu_list=menu.objects.all()
        return render(request,'pages/product/productlist.html',{'menu':menu_list})
        
    return render(request,'pages/product/editproduct.html',{'menu':menu_list,'catagory':costumer})

def mdelete(request,pk):
    del_list=menu.objects.get(id=pk).delete()
    menu_list=menu.objects.all()
    return render(request,'pages/product/productlist.html',{'menu':menu_list})

def madd(request):
    costumer=category.objects.all()    
    return render(request,'pages/product/addproduct.html',{'catagory':costumer})

def mdetail(request,pk):
    menu_list=menu.objects.get(id=pk)
    return render(request,'pages/product/productdetail.html',{'menu':menu_list})

