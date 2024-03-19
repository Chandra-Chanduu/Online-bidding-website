from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import ProductForm
from .models import Product
import time as t

# Create your views here.

# def timer(duration=20):
#     while duration:
#         duration-=1
#     return duration

def home(request):
    context={}
    products=Product.objects.all()
    context['products']=products
    #context['timer']=timer(20)
    return render(request,"home.html",context=context)

def add_product(request):
    if request.method=='POST':
        form=ProductForm(request.POST,request.FILES)
        if form.is_valid():
            result=form.save()
            print(result)
            return redirect('home')
    else:form=ProductForm()
    return render(request,"auction/add_product.html",{'form':form})

def bidding(request):
    return render(request,'auction/bidding.html')

