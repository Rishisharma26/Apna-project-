from asyncio.windows_events import NULL
from datetime import datetime
from django.db import models
from numpy import integer, product


# Create your models here.

class tableno(models.Model):
    tno=models.IntegerField()
    tstatus=models.IntegerField(default=0)
    
    
    def __str__(self):
        return str(self.tno) +'-'+ str(self.tstatus)




class tbooking(models.Model):

    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    email=models.EmailField(max_length = 50)
    phone=models.IntegerField(default=0)
    capacity=models.IntegerField()
    date =models.DateField()
    time=models.TimeField()
    rstatus=models.CharField(max_length=20,null= True) #request status
    tno=models.IntegerField(null=True)
    pic=models.FileField(upload_to='profile/',default='abc.jpg')
    # Tableno=models.ForeignKey(tableno,on_delete=models.CASCADE,default=NULL)
    
    def __str__(self):
        return self.fname + '/' + str(self.time)

class check(models.Model):
    cdate =models.DateField()
    ctime=models.TimeField()

class category(models.Model):
    cname=models.CharField(max_length=20)
    cid=models.CharField(max_length=20, default=0)

    def __str__(self):
        return self.cname + '/' + str(self.cid)

class menu(models.Model):
    item_name=models.CharField(max_length=20)
    item_price=models.IntegerField()
    item_desc=models.TextField(max_length=50,default="enjoy your food")
    item_category=models.ForeignKey(category, on_delete=models.CASCADE,default=1)
    pic=models.FileField(upload_to='menuimg/',default='abc.jpg',blank=True,null=True)
    availablity=models.CharField(max_length=20,default="available")

    
    def __str__(self):
        return self.item_name + '/' + str(self.item_price)

class clogin(models.Model):
    trans_id =models.AutoField(primary_key = True) #transaction id
    cust_id=models.ForeignKey(tbooking, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.trans_id)

    
class customercart(models.Model): #ye vala h
    order_id =models.AutoField(primary_key = True)
    item_id=models.ForeignKey(menu, on_delete=models.CASCADE)
    cust_number=models.ForeignKey(tbooking, on_delete=models.CASCADE)
    item_quantity = models.IntegerField(default=1)
    totalPrice = models.IntegerField(default=0)
    ctrans_id=models.ForeignKey(clogin, on_delete=models.CASCADE,default=7)
    def __str__(self):
        return str(self.order_id)

    def calculateTotal(self):
        totalPrice = self.item_quantity * self.item_id.item_price
        
        return totalPrice

    def save(self,*args, **kwargs):
        self.totalPrice = self.calculateTotal()
        super().save(*args, **kwargs)

        # dekh rha, haa

class yourorder(models.Model):
    order_id=models.IntegerField(default=1)
    order_item=models.ForeignKey(menu,on_delete=models.CASCADE,default=1)
    cust_number=models.IntegerField(default=1)
    item_quantity = models.IntegerField(default=1)
    totalPrice = models.IntegerField(default=0)
    payment_status=models.CharField(max_length=20,default='unpaid')
    process_status=models.CharField(max_length=20,default='accept')
    def __str__(self):
        return str(self.id)

class myorder(models.Model):
    order_id=models.IntegerField(default=1)
    order_item=models.ForeignKey(menu,on_delete=models.CASCADE,default=1)
    cust_number=models.IntegerField(default=1)
    item_quantity = models.IntegerField(default=1)
    totalPrice = models.IntegerField(default=0)
    payment_status=models.CharField(max_length=20,default='unpaid')
    process_status=models.CharField(max_length=20,default='accept')
    cust_details=models.ForeignKey(tbooking,on_delete=models.CASCADE,default=1)


class cart(models.Model):
    order_id =models.AutoField(primary_key = True)
    item_id=models.IntegerField()
    user_id=models.IntegerField()
# cust_number=models.ForeignKey(tbooking, on_delete=models.CASCADE)

class transaction(models.Model):
    trans_id =models.IntegerField()
    total_price=models.IntegerField()
    paid_status=models.CharField(max_length=20,default='unpaid')
    def __str__(self):
        return str(self.trans_id)
#transaction details
    

    