from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.
def sregister(request):
	if request.method=="POST":
		form=RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,'Registered Successfully')
			return redirect("slogin")	
	else:
		form=RegisterForm()
	return render(request,"sregisterlogin/supportregister.html",{"form":form})
		

def slogin(request):
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']
		user=auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request, user)
			return redirect("onsite")
		else:
			messages.info(request,"Invalid Username and Password")
			return redirect("slogin")
	else:
		return render(request,"sregisterlogin/slogin.html")


@login_required(login_url='slogin')
def sindex(request):
	return render(request,"sregisterlogin/sindex.html")

@login_required(login_url='slogin')
@staff_member_required
def onsite(request):
	return render(request,"dashboard/onsite.html")