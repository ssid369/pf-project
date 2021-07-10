from django.shortcuts import render
from .models import interest

def home(request):
	inter=interest.objects
	return render(request,'interests/home.html',{'inter':inter})