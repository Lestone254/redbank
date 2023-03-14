from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import login, logout,authenticate
# Create your views here.

def index(request):
	templatename="index/index.html"
	return render(request, templatename)


def enter(request):
	if request.user.is_authenticated:
		return redirect("account")
	templatename = "index/index.html"
	context= {}
	if request.method=="POST":
		username=request.POST['username']
		password=request.POST['password']
		next = request.GET.get("next")
		if User.objects.filter(username=username).exists():
			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)
				if not next == None:
					return redirect(next)
				return redirect("account")
			else:
				error ="The password you entered is incorrect !"
				context = {"error":error}
		else:
			error ="No user exists!"
			context={"error":error}
	return render(request, templatename, context)

def account(request):
	templatename="index/account.html"
	hospitals=Hospital.objects.all()
	context={"hospitals":hospitals}
	return render(request, templatename, context)








