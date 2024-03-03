from django.shortcuts import render
from django.http import HttpResponse
from .forms import ProductForm

# Create your views here.

def home(request):
    return render(request,"home.html")

def add_product(request):
    form=ProductForm(request.POST or None)
    if form.is_valid():
        result=form.save()
    return render(request,"auction/add_product.html",{'form':form})

