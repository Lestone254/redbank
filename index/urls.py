from django.urls import path
from .views import *
from django.contrib.auth.models import User

urlpatterns = [
	path("", index, name="index"),
	path("enter/", enter, name="enter"),
	path("account/", account, name="account"),
]
