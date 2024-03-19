from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib.auth import login,login,authenticate
from django.contrib.auth.models import User
from bidding.models import Product

# Create your views here.
def register_view(request):
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            user=form.save()
            authenticate(user)
            login(request,user)
            return redirect('/home')
    else:
        form=RegistrationForm()
    return render(request,"registration/register.html",{'form':form})

def profile_view(request):
    users=User.objects.all()
    print(users[0])
    context={
        #'users':users
    }
    return render(request,'profile.html',context=context)

def administration_view(request):
    products=Product.objects.all()
    if request.method=='POST':
        approved=request.POST.get('approved')
        product_id=Product.objects.filter(id=approved).first()
        if product_id.approved:
            product_id.approved=False
        else:
            product_id.approved=True
        product_id.save()
    context={
        'products':products
    }
    return render(request,'auction/administration.html',context=context)



