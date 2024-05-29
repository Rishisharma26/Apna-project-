
# # ////////////////
# from django.views.generic import TemplateView, FormView, CreateView, ListView, UpdateView, DeleteView, DetailView, View
# # ------template multiplication-----
# register = template.Library()

# @register.simple_tag()
# def multiplythis(qty, unit_price, *args, **kwargs):
#     # you would need to do any localization of the result here
#     multi = qty * unit_price
#     return multi

# # Create your views here.

# # solve the problem that when the cart is empty it throws an error--->solved
# # also non seller are able to add to cart , solve that too
# # create different table for the seller account and enable product add from there


# def home(request):
#     data = []
#     pro = products.objects.all()
#     category = categories.objects.all()
#     params = {'categories':category}
#     for cat in category:
#         cItem = products.objects.filter(productCategory=cat)
#         data.append(cItem)

#     if request.user.is_authenticated:
#         userProfile  = profile.objects.get(user = request.user)
#         params.update({'userProfile':userProfile.profileImage})
#         cart = customerCart.objects.filter(user=request.user)
#         if cart.exists():
            
#             params.update(values(request.user))
#             params.update({'totalCartItems':cart.count()})
#             # params = None
#             return render(request, 'myapp/home.html',{'products':pro,'carts':cart,'params':params,'data':data})
#         else:
#             params.update({'totalCartItems':0})
#             cart = None
#             return render(request, 'myapp/home.html',{'products':pro,'carts':cart,'params':params,'data':data})
            
#     params = {'totalCartItems':0,'categories':category}          
#     return render(request, 'myapp/home.html',{'products':pro,'params':params,'data':data})
    
# def logout_view(request):
#     logout(request)
#     return redirect('home')

# def login_view(request):
#     return redirect('/authentication/')

# def userProfile(request):
#     return render(request,'myapp/userprofile.html')

# def business_account(request):
#     pro = profile.objects.get(user=request.user)
#     if pro.is_seller:
#         return render(request, 'myapp/businessAccount.html')
#     else:
#         return render(request, 'myapp/addbusiness_account.html')

# def addBusinessAccount(request):
#     pro = profile.objects.get(user=request.user)
#     if pro.is_seller:
#         messages.info(request, 'you already have a business account, please create another profile to add Another Business account!')
#         return redirect('seller_addProducts')
#     if 'addBusinessAccount' in request.POST:
#         businessName=request.POST['businessName']
#         businessAddress = request.POST['businessAddress']
#         gstin = request.POST['gstin']
#         if request.user.is_authenticated:
            
#             pro = profile.objects.get(user=request.user)
#             if pro.is_seller:
#                 messages.info(request, 'you already have a business account, please create another profile to add Another Business account!')
#                 return redirect('business_account')
#             else:
                
#                 account = businessAccount(user=request.user,businessName=businessName,businessAddress=businessAddress,gstin=gstin)
#                 pro.is_seller=True
#                 account.save()
#                 pro.save()
#                 return redirect('home')
#         else:
#             messages.info(request,'you are not logged in')
#             return redirect('home')
#     else:
#         return render(request,'myapp/addbusiness_account.html')
            

# def seller_addProducts(request):
    
#     if 'addproduct' in request.POST:
#         productName=request.POST['productName']   
#         productPrice = request.POST['productPrice']   
#         productCategory=request.POST['productCategory']   
#         productSubCategory=request.POST['productSubCategory']   
#         productDetails=request.POST['productDetails']   
#         productInStock = request.POST['productInStock']
#         productCarMaker = request.POST['carMaker']
#         productCar = request.POST['cars']
#         productGstChoice = request.POST['productGst']
       
#         objProductGst = gstChoices.objects.get(gstDisplayName=productGstChoice)
#         objProductCategory = categories.objects.get(categoryName=productCategory)
#         objProductSubCategory = subcategories.objects.get(subcategoryName=productSubCategory)
#         objCarMaker = carMaker.objects.get(makerName=productCarMaker)
#         objProductCar = modelLine.objects.get(carName=productCar)
       
#         businessacc = businessAccount.objects.get(user=request.user)
        
#         pro = products(business=businessacc, productName=productName, productPrice=productPrice, productDetails=productDetails, productInStock=productInStock,productCategory=objProductCategory,productSubCategory=objProductSubCategory , carMaker=objCarMaker,car=objProductCar, productGst=objProductGst)
       
#         if len(request.FILES) != 0:
#             pro.productImage = request.FILES['uploadimage']
#             messages.info(request,len(request.FILES))

#             messages.info(request,'image added')
#             pro.save()
#             return redirect('seller_addProducts')
#         else:
#             messages.info(request,'image not added2')
#             return redirect('seller_addProducts')


#     else:
#         carmakers = carMaker.objects.all()
#         category = categories.objects.all()
#         chooseGst = gstChoices.objects.all()
#         params = {
#             'carmakers': carmakers,
#             'categories': category,
#             'gstChoices':chooseGst,
#         }
#         return render(request, 'myapp/seller_addProducts.html',{'params':params})
        

# def seller_viewProducts(request):
#     businessacc = businessAccount.objects.get(user=request.user)
#     product = products.objects.filter(business=businessacc)
#     return render(request, 'myapp/seller_viewProducts.html', {'products': product})
    
# def addtocart(request, productid):
#     if request.user.is_authenticated:
#         product = products.objects.get(id=int(productid))
#         cartitems = customerCart.objects.filter(user=request.user,product=product)
#         # cart = customerCart(user=request.user,product=product)
#         if 'tbproductQuantity' in request.POST:
#             addproductQuantity = request.POST['tbproductQuantity']
#             # addproductQuantity = 1
#             print(addproductQuantity)

#         else:
#             addproductQuantity = 1
#         if cartitems.exists():
#             cartitem = customerCart.objects.get(user=request.user,product=product)
#             cartitem.productQuantity += int(addproductQuantity)
#             cartitem.save()
#             print('printing int value')
#             print(int(addproductQuantity))

#         else:
#             print(addproductQuantity)
#             cart = customerCart(user=request.user,product=product,productQuantity=int(addproductQuantity))
#             cart.save()
#         messages.info(request, 'item added succesfully!')
#         # return redirect('home')
#         return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

#     else:
#         return redirect('/authentication/')


# def cart(request):
#     cartitems = customerCart.objects.filter(user=request.user)
#     if cartitems.exists():
        

#         params = values(request.user) 
#         params.update({'totalCartItems':cartitems.count()})
        
#         return render(request, 'myapp/cart.html', {'cartitems': cartitems, 'params':params})
#     else:
#         cartitems = None
#         param = {'totalCartItems':0}
#         return render(request,'myapp/cart.html',{'cartitems':cartitems,'params':params})

# def checkout(request):
#     carts = customerCart.objects.filter(user=request.user)
#     if carts.exists():
        
#         params = values(request.user)
#         params.update({'totalCartItems':carts.count()})
#     else:
#         params = {'totalCartItems':0}
#         carts = None
#         return render(request, 'myapp/checkout.html', {'customerinfos': customerinfo, 'carts': carts, 'params': params})
        
#     customerinfo = customerInfo.objects.filter(user=request.user)
#     if customerinfo.exists():
#         return render(request, 'myapp/checkout.html', {'customerinfos': customerinfo,'carts':carts,'params':params})
#     else:
#         customerinfo = None
#         if 'addAddress' in request.POST:
#             customer = customerInfo(user=request.user, customerFirstName=request.POST['customerFirstName'], customerLastName=request.POST['customerLastName'],customerAppartment=request.POST['customerAppartment'], customerCity=request.POST['customerCity'],customerState=request.POST['customerState'], customerPostalCode=request.POST['customerPostalCode'],customerPhone=request.POST['customerPhone'], customerCountry=request.POST['customerCountry'],customerStreet=request.POST['customerStreet'])
#             customer.save()
#             return redirect('checkout')
#         return render(request,'myapp/checkout.html',{'customerinfos':customerinfo,'carts':cart})
    
# def values(currentUser):
#     subtotal = customerCart.objects.filter(user=currentUser).aggregate(Sum('total'))
#     shippingCharge = 100
#     subtotal = subtotal['total__sum']
#     tax = round (subtotal * 18 / 100,2)
#     grandTotal = round(subtotal + shippingCharge + tax, 2)
#     param = {
#         'subtotal': subtotal,
#         'shippingCharge': shippingCharge,
#         'tax': tax,
#         'grandTotal':grandTotal
#     }
#     return param

# def placeOrder(request):
#     cartitems = customerCart.objects.filter(user=request.user)
#     oldorderidCounter = counters.objects.filter(id=1)
#     if oldorderidCounter.exists():
#         neworderidCounter = oldorderidCounter.orderidCounter + 1
#         oldorderidCounter.orderidCounter = neworderidCounter
#         oldorderidCounter.save()
#     else:
#         oldorderidCounter = 0
#         neworderidCounter = oldorderidCounter + 1
#     tbltransaction = transactions(user=request.user, orderid=neworderidCounter)
#     tbltransaction.save()
    
#     for cartitem in cartitems:
#         # businessacc = businessAccount.objects.get(user=)
#         pro = products.objects.get(id=cartitem.product.id)
#         order = orders(user=request.user,product=cartitem.product,seller=cartitem.product.business,productQuantity=cartitem.productQuantity,orderid=neworderidCounter)
#         order.save()
#         pro.productInStock = pro.productInStock - cartitem.productQuantity
#         pro.save()
#         cartitem.delete()
    
#     return render(request, 'myapp/ordersuccess.html',{'transactionid':neworderidCounter})
    
# def showeditproducts(request,productid):
#     product = products.objects.get(id=int(productid))
#     carmakers = carMaker.objects.all()
#     category = categories.objects.all()
#     chooseGst = gstChoices.objects.all()
#     params = {
#             'carmakers': carmakers,
#             'categories': category,
#             'gstChoices':chooseGst,
#         }
#     return render(request, 'myapp/editproducts.html', {'product': product,'params':params})
    
# def editproduct(request):
#     if 'update' in request.POST:
#         # product = products.objects.get(id=request.POST['productid'])
#         # product.productName = request.POST['productName']
#         # product.productPrice = request.POST['productPrice']
#         # product.productCategory = request.POST['productCategory']
#         # product.productDetails = request.POST['productDetails']
#         # product.productInStock = request.POST['productInStock']
#         # product.save()
#         productName=request.POST['productName']   
#         productPrice = request.POST['productPrice']   
#         productCategory=request.POST['productCategory']   
#         productSubCategory=request.POST['productSubCategory']   
#         productDetails=request.POST['productDetails']   
#         productInStock = request.POST['productInStock']
#         productCarMaker = request.POST['carMaker']
#         productCar = request.POST['cars']
#         productGstChoice = request.POST['productGst']
       
#         objProductGst = gstChoices.objects.get(gstDisplayName=productGstChoice)
#         objProductCategory = categories.objects.get(categoryName=productCategory)
#         objProductSubCategory = subcategories.objects.get(subcategoryName=productSubCategory)
#         objCarMaker = carMaker.objects.get(makerName=productCarMaker)
#         objProductCar = modelLine.objects.get(carName=productCar)
       
#         businessacc = businessAccount.objects.get(user=request.user)
#         product = products.objects.get(id=request.POST['productid'])
#         product.business = businessacc
#         product.productName = productName
#         product.productPrice = productPrice
#         product.productDetails = productDetails
#         product.productInStock = productInStock
#         product.productCategory = objProductCategory
#         product.productSubCategory = objProductSubCategory
#         product.carMaker = objCarMaker
#         product.car = objProductCar
#         product.productGst=objProductGst
#         product.save()
        
#         if len(request.FILES) != 0:
#             product.productImage = request.FILES['uploadimage']
#             messages.info(request,'image added')
#             product.save()
#             return redirect('seller_viewProducts')

#         else:
#             messages.info(request,'image not added2')
#             return redirect('seller_viewProducts')


#         return redirect('seller_viewProducts')
#     else:
#         carmakers = carMaker.objects.all()
#         category = categories.objects.all()
#         chooseGst = gstChoices.objects.all()
#         params = {
#             'carmakers': carmakers,
#             'categories': category,
#             'gstChoices':chooseGst,
#         }
#         return render(request,'myapp/editproducts.html',{'params':params})
    
# def deleteproduct(request, productid):
#     product = products.objects.get(id=int(productid)).delete()
#     return redirect('seller_viewProducts')
#     # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# # def productsPage(request):
# #     return render(request,'myapp/product.html')

# def allProducts(request):

#     if 'pageno' in request.GET:
#         pageno = int(request.GET['pageno'])
#     else:
#         pageno = 1
#     maxvalue = pageno * 10
#     minvalue = maxvalue - 10
#     params = {}

#     if 'category' in request.GET:
#         catergoryValue = request.GET['category']
#         categoryInUrl = 'True'
#         params.update({'categoryValue':catergoryValue})
#         compareCategory = categories.objects.get(categoryName=catergoryValue)
#         totalProducts = products.objects.filter(productCategory=compareCategory)
#     else:
#         categoryInUrl = False
#         totalProducts = products.objects.all()

#     if 'sortBy' in request.GET:
#         sort = request.GET['sortBy']
#         if sort == 'sortByName':
#             print('sorting by name')
#             totalProducts = totalProducts.order_by('productName')
#         elif sort == 'sortByPriceLowToHigh':
#             print('sorting by price')
#             totalProducts = totalProducts.order_by('productPrice')
#         elif sort == 'sortByPriceHighToLow':
#             print('sorting by price h tl')
#             totalProducts = totalProducts.order_by('-productPrice')
#         elif sort == 'sortByAverageRating':
#             print('sorting by price h tl')
#             totalProducts = totalProducts.order_by('-averageRating')

            


#     print(categoryInUrl)
#     product = totalProducts[minvalue:maxvalue]
#     productcount =totalProducts.count()
#     pages = math.ceil((productcount / 10))
#     category = categories.objects.all()
#     params.update({'categories': category,'categoryInUrl': categoryInUrl})
#     if request.user.is_authenticated:
#         cart = customerCart.objects.filter(user=request.user)
#         if cart.exists():
            
#             params.update(values(request.user))
#             params.update({'totalCartItems':cart.count()})
#             # params = None
#             return render(request, 'myapp/allProducts.html',{'carts':cart,'params':params , 'pros':product,'pages':range(1,pages+1),'productcount':productcount})
#         else:
#             params.update({'totalCartItems':0})
#             cart = None
#             return render(request, 'myapp/allProducts.html',{'carts':cart, 'pros':product,'params':params,'pages':range(1,pages+1),'totalCartItems':0})
#     return render(request, 'myapp/allProducts.html', {'pros': product,'pages':range(1,pages)})
    
# def viewSingleProduct(request,productid):
#     product = products.objects.get(id=int(productid))
#     reviews = productReview.objects.filter(product=product)
#     totalReviews = reviews.count()
#     # print('total reviews are : ', totalReviews)
#     if request.user.is_authenticated:
#         cart = customerCart.objects.filter(user=request.user)
#         if cart.exists():
            
#             params = values(request.user)
#             params.update({'totalCartItems':cart.count(),'productid':productid,'totalReviews':totalReviews})
#             # params = None
#             return render(request, 'myapp/viewSingleProduct.html',{'carts':cart,'params':params,'values':product,'reviews':reviews})
#         else:
#             cart = None
#             params = {'totalCartItems':0,'productid':productid,'totalReviews':totalReviews}
#             return render(request, 'myapp/viewSingleProduct.html',{'carts':cart,'values':product,'params':params,'reviews':reviews})
#     params = {'totalCartItems':0,'productid':productid,'totalReviews':totalReviews}
#     return render(request,'myapp/viewSingleProduct.html',{'values':product,'params':params,'reviews':reviews})
#     # pass


# def removeFromCart(request, productid):
#     pro = products.objects.get(id= int(productid))
#     cartitem = customerCart.objects.get(user=request.user,product=pro).delete()
#     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
#     # return render(request,'myapp/home.html')

# def seller_viewOrders(request):
#     business = businessAccount.objects.get(user=request.user)
#     order = orders.objects.filter(seller=business)
#     return render(request, 'myapp/seller_viewOrders.html', {'orders': order})
    
# def searchProducts(request):
#     cart = customerCart.objects.filter(user=request.user)
#     if cart.exists():
        
#         params = values(request.user)
#         params.update({'totalCartItems':cart.count()})
#     else:
#         params = {'totalCartItems':0}
#     if 'btnsearch' in request.POST:
#         searchValue = request.POST['search']
#         everyproduct = products.objects.filter(Q(productName=searchValue) | Q(productDetails=searchValue) | Q(productCategory=searchValue))
#         return render(request,'myapp/searchProducts.html',{'pros': everyproduct,'params':params})

#     return render(request, 'myapp/searchProducts.html', {'params': params})
    
# def addProductReview(request,productid):
#     if 'postReview' in request.POST:
#         product = products.objects.get(id=productid)
#         seller = product.business
#         user = request.user
#         reviewStars = request.POST['reviewStars']
#         product.totalNumberOfRatings  += 1
#         product.sumOfRatings += int(reviewStars)
#         product.save()
#         review = request.POST['review']
#         proReview = productReview(user = user, product=product, seller=seller,reviewStars=reviewStars,review=review)
#         proReview.save()
#     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
# def viewWishlist(request):
#     wNames = wishlistNames.objects.filter(user=request.user)
#     if wNames is not None:
#         data = []
#         wishlist = wishlistNames.objects.filter(user=request.user)
#         for wList in wishlist:
#             content = wishlistContent.objects.filter(wishlistName=wList)
#             data.append(content)

#         params = {
#             "wishlists" :data,
#         }
#     else:
#         params = {
#             'wishlists' : 'no wishlists exsists yet'
#         }
#     return render(request, 'myapp/wishlist.html',{'params':params})
    
# def contactus(request):
#     if 'sendMessage' in request.POST:
#         subject = request.POST['subject']
#         message = request.POST['message']
#         feedback = contactUs(user=request.user,subject=subject,message=message)
#         feedback.save()

#     return render(request, 'myapp/contactUs.html')

# def addWishlistName(request):
#     if 'addWishlist' in request.POST:
#         messages.info(request,'button pressed')
#         wishlistName = request.POST['wishlistName']
#         wName = wishlistNames(user = request.user,wishlistName=wishlistName)
#         wName.save()
#     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# def yourOrders(request):
#     data = []
#     transactionIds = transactions.objects.filter(user=request.user)
#     i = 1
#     for trs in transactionIds:
#         ordrs = orders.objects.filter(orderid=trs.orderid)
        
#         data.append(ordrs)
#     # i = 1
#     # somelist = [['string1','string2'],['string3','string4']]
#     # for dt in data:
#     #     val = str(i)
#     #     # print(dt[val])
#     #     for indt in dt[val]:
#     #         print(indt.product.productName)
#     #         print('/////////m')
#     #     print('-------nl')
#     #     i=i+1

#     allOrders = orders.objects.filter()
#     return render(request,'myapp/yourOrderss.html',{'data':data})

# def addingtowishlists(request):
#     checkboxes = request.POST.getlist('wishlistCheckboxes[]')
#     productid = request.POST['popupproductid']
#     product = products.objects.get(id=productid)

#     for checks in checkboxes:
#         wishlist = wishlistNames.objects.get(id=checks)
#         content = wishlistContent(products=product, wishlistName=wishlist)
#         content.save()
#     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
# def removeFromWishlist(request, wishlistid):
#     wishlistContent.objects.get(id=wishlistid).delete()
#     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



# # for generating pdf invoice
# from io import BytesIO
# from django.http import HttpResponse
# from django.template.loader import get_template
# from xhtml2pdf import pisa
# import os

# def fetch_resources(uri, rel):
#     path = os.path.join(uri.replace(settings.STATIC_URL, ""))
#     return path

# def render_to_pdf(template_src, context_dict={}):
#     template = get_template(template_src)
#     html  = template.render(context_dict)
#     result = BytesIO()
#     pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)#, link_callback=fetch_resources)
#     if not pdf.err:
#         return HttpResponse(result.getvalue(), content_type='application/pdf')
#     return None



# class GenerateInvoice(View):
#     def get(self, request, pk, *args, **kwargs):
#         try:
#             order_db = orders.objects.filter(orderid = pk)     #you can filter using order_id as well
#             # price = order_db.productQuantity * order_db.product.productPrice
#             name = order_db[0].user.username
#             email = order_db[0].user.email
#         except:
#             return HttpResponse("505 Not Found")
#         subtotal = orders.objects.filter(user=request.user,orderid=pk).aggregate(Sum('total'))
#         print(subtotal)
#         shippingCharge = 100
#         subtotal = subtotal['total__sum']
#         tax = round (subtotal * 18 / 100,2)
#         grandTotal = round(subtotal + shippingCharge + tax, 2)
#         param = {
#             'subtotal': subtotal,
#             'shippingCharge': shippingCharge,
#             'tax': tax,
#             'grandTotal':grandTotal
#         }
#         data = {
#             'orders': order_db,
#             'name': name,
#             'email':email,
#             'ordervalues': param,
#         }
#         pdf = render_to_pdf('myapp/invoice.html', data)
#         return HttpResponse(pdf, content_type='application/pdf')

#         # force download
#         # if pdf:
#         #     response = HttpResponse(pdf, content_type='application/pdf')
#         #     filename = "Invoice_%s.pdf" %(data['order_id'])
#         #     content = "inline; filename='%s'" %(filename)
#         #     #download = request.GET.get("download")
#         #     #if download:
#         #     content = "attachment; filename=%s" %(filename)
#         #     response['Content-Disposition'] = content
#         #     return response
#         # return HttpResponse("Not found")


# # //////////// for ajax///////////
# # AJAX REQUESTS------------------

# def viewingwishlists(request):
#     productid = request.GET['productid']
#     userid = request.GET['userid']
#     activeuser = User.objects.get(id=userid)
#     wishlistnames = wishlistNames.objects.filter(user=activeuser)
#     print('productid: '+productid)
#     print('userid: '+userid)
#     # print('maker: ' + getmaker.makerName)
#     # getcars = modelLine.objects.filter(maker=getmaker)
#     # for car in getcars:
#     #     print('cars: ' + car.carName)
#     data = []
#     for name in wishlistnames:
#         item = {
#             'wishlistname': name.wishlistName,
#             'wishlistid': name.id,
            
#         }
#         data.append(item)
#     # maker = 'working'
#     return JsonResponse({'data': data})
    



# def carmakerdropdown(request):
#     maker = request.GET['maker']
#     getmaker = carMaker.objects.get(makerName=maker)
#     # print('maker: ' + getmaker.makerName)
#     getcars = modelLine.objects.filter(maker=getmaker)
#     # for car in getcars:
#     #     print('cars: ' + car.carName)
#     data = []
#     for car in getcars:
#         item = {
#             'carname': car.carName,
#             'carid' : car.id
#         }
#         data.append(item)
#     # maker = 'working'
#     return JsonResponse({'data': data})
    
# def categorydropdown(request):
#     categoryName = request.GET['category']
#     print('coming to the view function')
#     print(categoryName)
#     getCategory = categories.objects.get(categoryName=categoryName)
#     # print('maker: ' + getmaker.makerName)
#     getSubCategory = subcategories.objects.filter(category=getCategory)
#     # for car in getcars:
#     #     print('cars: ' + car.carName)
#     data = []
#     for subcat in getSubCategory:
#         item = {
#             'subCategoryName': subcat.subcategoryName,
        
#         }
#         data.append(item)
#     # maker = 'working'
#     return JsonResponse({'data':data})