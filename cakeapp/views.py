from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from cakeapp.models import Cake,Cart,Order
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q
import random



# Create your views here.

def home(request):
    userdata=request.user.id
    obj=Cake.objects.filter(is_active=True)
    context={'cake':obj}
    return render(request,"index.html",context)


def register(request):
    if request.method=='GET':
        return render(request,'register.html')
    else:
        u=request.POST['uname']
        p=request.POST['upass']
        c=request.POST['ucpass']
        uobj=User.objects.create(username=u,email=u)
        uobj.set_password(p)
        uobj.save()
        return redirect('/register')
    


def user_login(request):
    if request.method=='GET':
        return render(request,'login.html')
    else:
        u=request.POST['uname']
        p=request.POST['upass']
        a=authenticate(username=u,password=p)
        if a is not None:
            print(a)
            print(a.password,a.id)
            login(request,a)
            return redirect('/')
        else:
            return HttpResponse("Login failed")
        
def user_logout(request):
    logout(request)
    return redirect("/") 

def contact_us(request):
    return render(request,"contact.html")

def about_us(request):
    return render(request,"about.html")

def menucard(request):
    return render(request,'menu.html')

def product_detail(request,pid):
    obj=Cake.objects.filter(id=pid)
    context={'cake':obj}
    return render(request,'productdetail.html',context)

def addtocart(request,pid):
    if request.user.is_authenticated:
        userid=request.user.id
        u=User.objects.filter(id=userid)
        p=Cake.objects.filter(id=pid)
        obj=Cart.objects.create(uid=u[0],pid=p[0],cprice=p[0].price)
        obj.save()
        return redirect('/')
    else:
        return redirect("/cart")


def cart(request):
    c=Cart.objects.filter(uid=request.user.id)
    s=0
    cnt=0
    for i in c:
        cnt+=1
        s=s+(i.pid.price * i.qty)
    context={'cake':c,'total':s,'cnt':cnt}
    print("sum:",s)
    return render(request,"cart.html",context)



def updateqty(request,qv,cid):
    print(type(qv))
    c=Cart.objects.filter(id=cid)
    if qv=='1':
        qty=c[0].qty + 1
        c.update(qty=qty,cprice=c[0].pid.price*qty)
        return redirect("/cart")
    elif c[0].qty>1:
        qty=c[0].qty - 1
        c.update(qty=qty,cprice=c[0].pid.price*qty)
        return redirect("/cart")
    else:
        return redirect("/cart")


def catfilter(request,cv):
    if cv == '1':
        obj=Cake.objects.filter(cat=1)
        context={'cake':obj}
        return render(request,'index.html',context)
    elif cv == '2':
        obj=Cake.objects.filter(cat=2)
        context={'cake':obj}
        return render(request,'index.html',context)
    elif cv == '3':
        obj=Cake.objects.filter(cat=3)
        context={'cake':obj}
        return render(request,'index.html',context)
    elif cv == '4':
        obj=Cake.objects.filter(cat=4)
        context={'cake':obj}
        return render(request,'index.html',context)
    elif cv == '5':
        obj=Cake.objects.filter(cat=5)
        context={'cake':obj}
        return render(request,'index.html',context)
    elif cv == '6':
        obj=Cake.objects.filter(cat=6)
        context={'cake':obj}
        return render(request,'index.html',context)
    else:
        obj=Cake.objects.filter(cat=7)
        context={'cake':obj}
        return render(request,'index.html',context)


def range(request):
    if request.method=='GET':
        min=request.GET['min']
        max=request.GET['max']
        c1=Q(price__gte=min)
        c2=Q(price__lte=max)
        c=Cake.objects.filter(c1 & c2)
        context={'cake':c}
        return render(request,'index.html',context)


def placeorder(request):
    c=Cart.objects.filter(uid=request.user.id)
    oid=random.randrange(1000,9999)
    print(oid)
    for x in c:
        obj=Order.objects.create(order_id=oid,pid=x.pid,uid=x.uid,qty=x.qty)
        obj.save()
        x.delete()
    return redirect('/makepayment')

import razorpay

def makepayment(request):
    client = razorpay.Client(auth=("rzp_test_scCiQf59kX7GfU", "IaTvZbo9qiG67It4bez6CSba"))

    data = { "amount": 500, "currency": "INR", "receipt": "order_rcptid_11" }
    payment = client.order.create(data=data)
    data={'payment':payment}
    return render(request,"pay.html",data)

