from django.shortcuts import render
from .models import Menu,Option
# Create your views here.
def menu_list(request):
	menus = Menu.objects.filter()
	return render(request,'menu/list.html',{'menus': menus})

def menu_create():
	pass

def menu_view():
	pass

def menu_update():
	pass			