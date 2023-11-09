from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import CustomRegsiterForm

def register(request):
    if request.method=="POST":
        register_form=CustomRegsiterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,('New User Account Created, Login to Get Started!'))
            return redirect('register')
        
    
    else:
        register_form=CustomRegsiterForm()
    return render(request,'register.html',{ 'register_form': register_form })