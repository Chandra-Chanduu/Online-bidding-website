from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib.auth import login,login,authenticate

# Create your views here.
def register_view(request):
    if request.method=='POST':
        form=RegistrationForm(None or request.POST)
        if form.is_valid:
            user=form.save()
            #authenticate(request,user)
            login(request,user)
            redirect('')
    else:
        form=RegistrationForm()
    return render(request,"registration/register.html",{'form':form})

