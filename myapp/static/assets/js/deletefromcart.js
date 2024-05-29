function deletefromcart(productid,userid){
    console.log('comming to delete from cart');
    console.log(productid);

    
  console.log('coming to ajax function')
  var select = document.getElementById('gettingdata')
  // var value = select.options[select.selectedIndex].value
  $.ajax({
    type: 'GET',
    url: '/deletefromcartajax/',
    data: {
      'productid': productid,
      'userid': userid,
    },
    success: function (response) {
        const data = response.data;
        console.log('image path isad:');
        // var val = data[0].productImage;
        // console.log(val);
        var cart = document.getElementsByClassName('js-cd-cart'),
        cartBody = cart[0].getElementsByClassName('cd-cart__body')[0],
        cartList = cartBody.getElementsByTagName('ul')[0];
        var productAdded='';
        console.log(data[0].status)
        if (data[0].status == 'False'){   
            console.log('status:')
            console.log(data[0].status)
            cartList.innerHTML='<h1>Your Cart is Empty!</h1>';

        }
        else{  
        $.each(data, function(k, v)
        {
            console.log('status:')
            console.log(data[k].status)
            console.log('in for each.......')
            console.log(data[k].productName)
         productAdded += '<li class="cd-cart__product"><div class="cd-cart__image"><a href="#0"><img src="'+data[k].productImage+'" alt="image"></a></div><div class="cd-cart__details"><h3 class="truncate"><a href="#0">'+ data[k].productName +'</a></h3><span class="cd-cart__price">'+ data[k].productPrice +'<a href="#" onclick=deletefromcart('+ data[k].productId +')>delete Product</a></span><div class="cd-cart__actions"><a href="#0" class="cd-cart__delete-item">Delete</a><div class="cd-cart__quantity"><label for="cd-product-'+ data[k].productId +'">Qty</label><span class="cd-cart__select"><select class="reset" id="cd-product-'+ data[k].productId +'" name="quantity"><option value="1">1</option><option value="2">2</option><option value="3">3</option><option value="4">4</option><option value="5">5</option><option value="6">6</option><option value="7">7</option><option value="8">8</option><option value="9">9</option></select><svg class="icon" viewBox="0 0 12 12"><polyline fill="none" stroke="currentColor" points="2,4 6,8 10,4 "/></svg></span></div></div></div></li>';
         cartList.innerHTML=productAdded;
        });
         
    }
          // productImage = "C:\Users\DELL\Downloads\myproject\menuimg\brain1.jpg"
          
      //   cartList.insertAdjacentHTML('beforeend', productAdded);
    },
    error: function (error) {
      console.log('no success')
      console.log('error', error)
    },
  })
 


}