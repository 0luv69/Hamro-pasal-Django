from django.shortcuts import render,redirect,get_object_or_404
from .models import *
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required,user_passes_test
import random
import datetime


def list_on_sale(product_list):
    sorted_list = sorted(product_list, key=lambda x: x.sale, reverse=True)
    return sorted_list

def list_higest_price(product_list):
    sorted_list= sorted(product_list, key= lambda x: x.amount, reverse=True )
    return sorted_list

def list_lowest_price(product_list):
    sorted_list= sorted(product_list, key= lambda x: x.amount, reverse=False )
    return sorted_list

def list_rating(product_list):
    sorted_list= sorted(product_list, key= lambda x: x.ratting, reverse=True )
    return sorted_list

def short_request(request, short_id):
    if short_id == 'none':
        return redirect('home')
    else:
        return home_pg(request, short_on=short_id )



def home_pg(request, short_on='none'):
    products = list(Product.objects.all())
    if short_on == 'sale':
        products= list_on_sale(products)
    elif short_on == 'H_price':
        products= list_higest_price(products)    
    elif short_on == 'L_price':
        products= list_lowest_price(products) 
    elif short_on == 'rate':
        products= list_rating(products) 
     


    total_items_num=0
    if request.user.is_authenticated:
        cartsinfo, create= carts_info.objects.get_or_create(user = request.user)
        total_items_num = cartsinfo.total_items


    context= {
         'products':products,
         "total_items_num":total_items_num,
         'short_on':short_on

    }
    return render(request, 'page/index.html',context )

@login_required(login_url="login")
def add_cart(request,id):
    cartsinfo, created= carts_info.objects.get_or_create(user = request.user)
    cartsinfo.total_items +=1

    product_instance= get_object_or_404(Product, id = id)
    itemsincart, created= itemsInCart.objects.get_or_create(cart_info= cartsinfo, product = product_instance )
    itemsincart.quantity +=1

    cartsinfo.save()
    itemsincart.save()
    return redirect('home')



@login_required(login_url="login")
def cart_pg(request):
    if request.user.is_authenticated:
        cartsinfo= carts_info.objects.filter(user = request.user)[0]
        itemsincart= itemsInCart.objects.filter(cart_info= cartsinfo)

        cartsinfo, create= carts_info.objects.get_or_create(user = request.user)
        total_items_num = cartsinfo.total_items
        context= {
            'itemsincart':itemsincart,
            'total_items_num':total_items_num,
        }
        return render(request, 'page/cart.html', context)

@login_required(login_url="login")
def rmv_cart(request,id):
    if request.user.is_authenticated:
            cartsinfo, created= carts_info.objects.get_or_create(user = request.user)
            product_instance= get_object_or_404(Product, id = id)
            itemsincart, created= itemsInCart.objects.get_or_create(cart_info= cartsinfo, product = product_instance )

            cartsinfo.total_items -=itemsincart.quantity
            itemsincart.delete()
            cartsinfo.save()
            return redirect('cart')

@login_required(login_url='login')
def get_data(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            responce_reason = data.get('reason')
            if responce_reason == 'get_previous_data':
                checkoutinfo = CheckOutInfo.objects.get(user=request.user)
                return JsonResponse({'fill_data_received': checkoutinfo})






            return JsonResponse({'fill_data_received': responce_reason})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    else:
        # Handle requests other than POST
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)


@login_required(login_url="login")
def checkout_pg(request):
    if request.user.is_authenticated:
        cartsinfo= carts_info.objects.filter(user = request.user)[0]
        total_items_num = cartsinfo.total_items
        if total_items_num >=1:
            if request.method == "POST":
                data = request.POST
                f_name, l_name=data['fname'],data['lname']

                phnum, email= data['phone'],data['email']

                country, state, city, streetname, fulladdress= data['country'],data['state'],data['city'],data['streetname'],data['fulladdress'],
            
                order_notes= data['order_notes']

                #user
                user_ins= request.user
                if user_ins.first_name != f_name:
                    user_ins.first_name = f_name 
                if  user_ins.last_name != l_name:
                    user_ins.last_name = l_name   
                user_ins.save()    

                # check out info
                checkoutinfo, created= CheckOutInfo.objects.get_or_create(user=user_ins)
                checkoutinfo.Phonenum= phnum
                checkoutinfo.shipemail=email

                checkoutinfo.Country=country
                checkoutinfo.State= state
                checkoutinfo.city= city
                checkoutinfo.Street_Name = streetname
                checkoutinfo.Full_Address= fulladdress

                checkoutinfo.Order_Notes= order_notes
                checkoutinfo.save()
        


                #shipping_info
                shippinginfos= shipping_info.objects.create(checkout_info=checkoutinfo )
                r_num1 = random.randint(1000, 9999)
                r_num2 = random.randint(1000, 9999)
                current_year = datetime.datetime.now()
                shippinginfos.shipping_number = f"{r_num1}{current_year.year}{r_num2}--{shippinginfos.id}"
                shippinginfos.deliver_Date_on= current_year + datetime.timedelta(days=8)

                shippinginfos.save()

                #checkout_products
                itemsincart= itemsInCart.objects.filter(cart_info= cartsinfo)
                for each_item in itemsincart:
                    checkoutproduct, created = checkout_products.objects.get_or_create(shippinginfo= shippinginfos, product= each_item.product)
                    checkoutproduct.quantity= each_item.quantity
                    checkoutproduct.save()

                itemsincart.delete()   
                cartsinfo.total_items=0
                cartsinfo.save()


                checkout_product=  checkout_products.objects.filter(shippinginfo= shippinginfos)
                context= {
                    'shipping_info':shippinginfos,
                    'itemsincart':checkout_product,
                    'checkoutinfo':checkoutinfo
                }

                return render(request, 'page/checkout.html', context)

            else:
                    cartsinfo= carts_info.objects.filter(user = request.user)[0]
                    itemsincart= itemsInCart.objects.filter(cart_info= cartsinfo)
                    total_items_num = cartsinfo.total_items
                    context= {
                        'procude_pg':1,
                        'total_items_num':total_items_num,
                        'itemsincart':itemsincart,
                    }
                    return render(request, 'page/checkout.html', context)
        return redirect('cart')

@login_required(login_url="login")
def producthistory_pg(request):
    if request.user.is_authenticated:
        try:
            checkoutinfo = CheckOutInfo.objects.get(user=request.user)
            shippinginfos= shipping_info.objects.filter(checkout_info=checkoutinfo )

            all_checkout= []
            for each in shippinginfos:
                all_checkout.append(checkout_products.objects.filter(shippinginfo= each))

            context = {
                 'checkoutinfo':checkoutinfo,
                 'checkout_product':all_checkout,
                 'shippinginfos':shippinginfos


            }





        except:context={'no_history':1}                 
         
        return render(request, 'page/history.html', context)
         



def login_pg(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            data = request.POST
            uname= data['uname']
            psd = data['psd']
            if not User.objects.filter(username= uname).exists():
                    messages.add_message(request, messages.INFO, "Invalid User name")
                    return redirect('login')
            user= authenticate(username= uname, password= psd)
            if user is None:
                    messages.add_message(request, messages.INFO, "Invalid Password")
                    return redirect('login')            
            else:
                messages.add_message(request, messages.INFO, "Success")
                login(request,user) #session send
                return redirect('home')
    
        return render(request, 'page/login.html')

def logout_pg(request):
    logout(request)        
    return redirect('login')

def signup_pg(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:    
        if request.method=="POST":
            data = request.POST
            email=data['email']
            user_name= data['uname']
            password= data['psw']

            if User.objects.filter(username= user_name).exists():
                messages.add_message(request, messages.INFO, "User already Exits plz try again.")
                return redirect('signup')
            else:
                messages.add_message(request, messages.INFO, "Account Created Sucessfully")
                user = User.objects.create(username=user_name, email =email, password= password)
                user.set_password(password)
                user.save()
                return redirect('login')
        return render(request, 'page/signup.html')


