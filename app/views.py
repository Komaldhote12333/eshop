from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def index(request):
    products = Product.objects.all()
    
    data ={
        'products' : products
    }
    print(data)
    return render(request,"index.html",data)




def products(request):
 
    products = Product.objects.all()
    money = Filter_Price.objects.all()
    category = Category.objects.all()
    colors = Color.objects.all()
    brands = Brand.objects.all()
    catid = request.GET.get('catid')
    priceid = request.GET.get('priceid')
    colorsid = request.GET.get('colorsid')
    branid = request.GET.get('branid')
    atoz = request.GET.get('atoz') 
    ztoa = request.GET.get('ztoa') 
    ltoh = request.GET.get('ltoh')
    htol = request.GET.get('htol')  
    new = request.GET.get('new')  
    old = request.GET.get('old')  
       
       
    
    
    
    if catid:
        products = Product.objects.filter(category=catid)
        
    elif priceid:
        products = Product.objects.filter(filter_price=priceid)
        
    elif colorsid:
        products = Product.objects.filter(color=colorsid)
        
    elif branid:
        products = Product.objects.filter(brand=branid)   
            
    elif atoz:
        products = Product.objects.order_by("name")
        
    elif ztoa:
        products = Product.objects.order_by('-name')
        
    elif ltoh:
        products = Product.objects.order_by('price')  
            
    elif htol:
        products = Product.objects.order_by('-price')
        
    elif new:
        products = Product.objects.filter(condition="new")
        
    elif old:
        products = Product.objects.filter(condition="old")         
           
        
    else:
        products = Product.objects.all()
            
        
    
    data ={
        'products' : products,
        'category' :category,
        'money':money,
        'colors':colors,
        'brands':brands,
    }
    
    return render(request,"product.html",data)


def search(request):
    serchname = request.GET.get("serchname")
    products = Product.objects.filter(name__icontains =serchname)
    if products:
        return render(request,"search.html",{'products' : products}) 
    else:
        return render(request,"search.html")
        
        
        
def quickview(request,id):
    type(id)
    products = Product.objects.all()
    prod = Product.objects.get(id=id) 
    data={
        "prod":prod,
        'products' : products,
    }
    print(prod)
    return render(request,"quickview.html",data)
            
            
def login(request):
    return render(request,'login.html')            



def registerdone(request):
    error=None
    if request.method =="POST":
        unm=request.POST['username'] 
        pwd=request.POST['password']
        email=request.POST['email']
        try:
            user=User.objects.get(username=unm)
            error= "this username or email already exixt try once more"
            return render(request,'login.html',{"error":error})
        except:
            if(len(unm)<10):
                error= "username should be 10 charector logng"
                return render(request,'login.html',{"error":error})
            if(len(email)<18):
                error= "email should be 15 charector logng"
                return render(request,'login.html',{"error":error})
                
            else:    
                user=User.objects.create_user(username=unm,password=pwd,email=email)
                error= "sucssesfully loged in"
                user.save()
                request.session["userid"] = user.id
                return render(request,'login.html',{"error":error})
    else:
        return render(request,'login.html')
    
    
    
def logindone(request):
    if request.method=="POST":
        unm=request.POST['username']
        pwd=request.POST['password']
        user=auth.authenticate(username=unm,password=pwd)
        if user is not None:
            auth.login(request,user)
            request.session["userid"] = user.id
            return redirect('home')
        else:
            return render(request,'login.html')
    else:
        return render(request,'login.html')    
    







@login_required(login_url="login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="login")
def item_decrement(request, id):
    cart = Cart(request)
    try:
        product= Product.objects.get(id=id)
        cart.decrement(product=product)
        return redirect("cart_detail")
    except:     
      return redirect("cart_detail")


@login_required(login_url="login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="login")
def cart_detail(request):
    return render(request, 'cart.html')


def logout(request):
    auth.logout(request)
    request.session.clear()
    return redirect("index")

@login_required(login_url="login")
def contact(request):
    return render(request, 'contact.html')

@login_required(login_url="login")
def contactsavr(request):
    error=None
    if request.method == "POST":
        
        name = request.POST['name']
        email =request.POST['email']
        subject=request.POST['subject']
        imformation=request.POST['imformation']
        con = Contact(name=name,email=email,subject=subject,imformation=imformation)
        if con:
           try:   
                send_mail(
                        subject=subject,
                        message=imformation,
                        from_email=settings.EMAIL_HOST_USER,
                        recipient_list=['komaldhote9981@gmail.com'])
                
                con.save()
                return redirect("index")
           except:
               error="network connection error" 
               return render(request, 'contact.html',{"error":error})                 
                
        else:
            return redirect("index")
    else:
        return redirect("index")
    
@login_required(login_url="login")
def checout(request):
    return render(request, 'checout.html')   
     
  
@login_required(login_url="login")  
def order(request):
    return render(request,"checout.html")     
   
@login_required(login_url="login")
def ordertaking(request):
    eroor=None
    if request.method == "POST":
        cart = request.session.get("cart")
        ids = list(request.session.get("cart").keys())
        products = Product.objects.filter(id__in=ids)
        usernamme = request.session.get("userid")
        firstname=request.POST.get("firstname")
        lastnam=request.POST.get("lastnam")
        country=request.POST.get("country")
        housnum=request.POST.get("housnum")
        city=request.POST.get("city")
        state=request.POST.get("state")
        zipcode=request.POST.get("zipcode")
        phone=request.POST.get("phone")
        email=request.POST.get("email")
        additninal=request.POST.get("additninal")
       
        
        for product in products:
            order = Orderform(
                user = User(id=usernamme),
                product=product,
                firstname=firstname,
                lastnam=lastnam,
                country=country,
                housnum=housnum,
                city=city,
                state=state,
                zipcode=zipcode,
                price = product.price,
                quntity = cart.get(str(product.id)),
                phone=phone,
                email=email,
                additninal=additninal,
            )
            
            try:
                allitem =( firstname,lastnam,country,housnum,city,state,zipcode,email,additninal)
                send_mail(
                    subject= allitem,
                    message = product.name,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=['komaldhote9981@gmail.com'])
                
                order.save()
                return redirect("index")
            except:
                eroor="network connection lost"
                return render(request,"checout.html",{'eroor':eroor})  
                  
        request.session.get("cart").clear()    
        return redirect("index")
        
        
       
    else:
            
         return render(request, 'checout.html')


@login_required(login_url="login")
def ordershow(request):
    usernamme = request.session.get("userid")
    order=Orderform.objects.filter(user=User(id=usernamme))
   
    return render(request, 'ordershow.html',{'order':order})

@login_required(login_url="login")
def update(request):
    usernamme = request.session.get("userid")
    oid = request.GET.get('oid')
    upd=Orderform.objects.get(id=oid)
    print(upd)
    return render(request,'update.html',{'upd':upd})


def about(request):
    team = Team.objects.all()
    return render(request,'about.html',{"team":team})


def delet(request):
    
    dee=request.GET.get("de")
    dele= Orderform.objects.get(id=dee)
    dele.delete()
    usernamme = request.session.get("userid")
    order=Orderform.objects.filter(user=User(id=usernamme))
   
    return render(request, 'ordershow.html',{'order':order})    
   
    


                      