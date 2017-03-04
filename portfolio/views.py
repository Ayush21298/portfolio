from django.shortcuts import render
from .models import Pers_Info

def info(request, entry_no):
	return render(request , 'portfolio/info.html', {'entry_no':entry_no})