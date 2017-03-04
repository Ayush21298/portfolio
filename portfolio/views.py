from django.shortcuts import render
from .models import Pers_Info

def info(request, entry_no):
	p = Pers_Info.objects.get(entry=entry_no)
	return render(request , 'portfolio/info.html', {'p':p})