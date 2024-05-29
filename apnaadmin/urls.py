from django import views
from django.urls import path
# from . import views 
from . import views
urlpatterns = [
    path('',views.aindex),
    path('orders/',views.orders,name='orders'),
    path('rtable/',views.rtable,name='rtable'),#registration table
    path('mtable/',views.mtable,name='mtable'),#menu table
    path('editmenu/<int:pk>/',views.medit,name='medit'),#menu edit
    path('deletemenu/<int:pk>/',views.mdelete,name='mdelete'),#menu edit
    path('detailmenu/<int:pk>/',views.mdetail,name='mdetail'),#menu details
    path('status/',views.status,name='status'),#menu details
    path('additem/',views.madd,name='madd'),#menu add items
    
]