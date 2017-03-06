from django.shortcuts import render
from .models import Pers_Info
	
def index(request):
	students = Pers_Info.objects.all()
	return render(request, 'portfolio/index.html',{'students':students})

def info(request, entry_no):
	p = Pers_Info.objects.get(entry=entry_no)
	return render(request , 'portfolio/info.html', {'p':p})

def home(request):
	return render(request, 'portfolio/home.html',{})	

def mail(request):
	return render(request, 'portfolio/mail.html',{})

def ack(request):
	return render(request, 'portfolio/ack.html',{})
	
