from urllib import request
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'index.html')
    
def register(request):
    if request.method == "POST":
	
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = {
            "username" : form.cleaned_data["username"],
            "email" : form.cleaned_data["email"],
            "password1" : form.cleaned_data["password1"],
            "password2" : form.cleaned_data["password2"]
            }
            user = form.save()
            login(request, user)
            messages.success(request,"Registration successful." )
            return render(request,"index.html",{"user":user})
        else:
            messages.info(request, "Unsuccessful registration. Invalid information.")

    form = NewUserForm()
    return render(request,"register.html", context={"form":form})



