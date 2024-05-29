from django import views
from django.urls import path
from . import views
urlpatterns = [
path('',views.index),
path('home/',views.index,name='home'),
path('register-reservation.html/',views.booking, name='booking'),
path('otp/',views.otp,name='otp'),
path('login/',views.login,name='login'),
path('logout/',views.logout,name='logout'),
path('dashboard/',views.dashboard,name='dashboard'),
path('index2/',views.login,name='index2'),
path('menu/',views.menue,name='menue'),
path('cart/',views.cart,name='cart'),
path('order/',views.order,name='order'),
path('addtocartajax/',views.addtocartajax,name='addtocartajax'),
path('deletefromcartajax/',views.deletefromcartajax,name='deletefromcartajax'),
path('orderDetails/',views.checkout,name='checkout'),
path('checkout/',views.checkout1,name='checkout1'),
]