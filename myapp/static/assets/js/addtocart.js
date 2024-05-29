function addtocart(productid) {
  console.log('coming to ajax function')
  var value = productid
  var select = document.getElementById('gettingdata')
  // var value = select.options[select.selectedIndex].value
  $.ajax({
    type: 'GET',
    url: '/addtocartajax/',
    data: {
      'productid': value,
    },
    success: function (response) {
      const data = response.data;
      console.log('image path isad:');
      var val = data[0].productImage;
      console.log(val);
      var cart = document.getElementsByClassName('js-cd-cart'),
      cartBody = cart[0].getElementsByClassName('cd-cart__body')[0],
      cartList = cartBody.getElementsByTagName('ul')[0];
      var productAdded='';
      $.each(data, function(k, v)
      {
          console.log('in for each.......')
          console.log(data[k].productName)
          console.log(data[k].totalPrice)
       productAdded += '<li class="cd-cart__product"><div class="cd-cart__image"><a href="#0"><img src="'+data[k].productImage+'" alt="image"></a></div><div class="cd-cart__details"><h3 class="truncate"><a href="#0">'+ data[k].productName +'</a></h3><span class="cd-cart__price">'+ data[k].totalPrice +'<a href="#" onclick=deletefromcart('+ data[k].productId +')>delete Product</a></span><div class="cd-cart__actions"><a href="#0" class="cd-cart__delete-item">Delete</a><div class="cd-cart__quantity"><label for="cd-product-'+ data[k].productId +'">Qty</label><span class="cd-cart__select"><select class="reset" id="cd-product-'+ data[k].productId +'" name="quantity"><option value="1">1</option><option value="2">2</option><option value="3">3</option><option value="4">4</option><option value="5">5</option><option value="6">6</option><option value="7">7</option><option value="8">8</option><option value="9">9</option></select><svg class="icon" viewBox="0 0 12 12"><polyline fill="none" stroke="currentColor" points="2,4 6,8 10,4 "/></svg></span></div></div></div></li>';
      });
        // productImage = "C:\Users\DELL\Downloads\myproject\menuimg\brain1.jpg"
        
    //   cartList.insertAdjacentHTML('beforeend', productAdded);
            document.getElementsByClassName('cd-cart__checkout').innerHTML = 'checkout 1500';
			cartList.innerHTML=productAdded;
    },
    error: function (error) {
      console.log('no success')
      console.log('error', error)
    },
  })
  console.log(value)

  console.log('working :', value)
}
