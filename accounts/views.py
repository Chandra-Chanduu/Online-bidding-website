from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib.auth import login,login,authenticate

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


