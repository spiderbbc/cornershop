from django.shortcuts import render,redirect,get_object_or_404
from .models import Menu,Option
from .forms import MenuCreateForm,OptionCreateForm
# Create your views here.
def menu_list(request):
	menus = Menu.objects.filter()
	return render(request,'menu/list.html',{'menus': menus})

def menu_create(request):
	if request.method == 'POST':
		form = MenuCreateForm(request.POST)
		if form.is_valid():
			menu = form.save(commit=False)
			menu.user = request.user
			menu.save()
			return redirect('menu:view', menu_id=menu.id)
	else:
		form = MenuCreateForm()
	return render(request,'menu/create.html',{'form': form})

def menu_view(request,menu_id):
	menu = get_object_or_404(Menu, id = menu_id)
	return render(request,'menu/view.html',{'menu': menu})

def menu_update(request,menu_id):
	menu = get_object_or_404(Menu, id = menu_id)
	form = MenuCreateForm(request.POST or None, instance= menu)
	context = {'form': form}
	if form.is_valid():
		menu = form.save(commit=False)
		menu.user = request.user
		menu.save()
		return redirect('menu:index')
	else:
		context = {'form': form}
	return render(request,'menu/update.html',{'form': form})		

def option_create(request,menu_id):
	menu = get_object_or_404(Menu, id = menu_id)
	if request.method == 'POST':
		form = OptionCreateForm(request.POST)
		if form.is_valid():
			option = form.save(commit=False)
			option.menu = menu
			option.save()
			return redirect('menu:view', menu_id=menu.id)
	else:
		form = OptionCreateForm()
	return render(request,'option/create.html',{'form': form})

def option_update(request,option_id):
	option = get_object_or_404(Option, id = option_id)
	form = OptionCreateForm(request.POST or None, instance= option)
	context = {'form': form}
	if form.is_valid():
		option = form.save(commit=False)
		menu = option.menu
		option.save()
		return redirect('menu:view', menu_id=menu.id)	
	else:
		context = {'form': form}
	return render(request,'menu/update.html',{'form': form})

def option_delete(request,option_id):
	option = get_object_or_404(Option, id = option_id)
	menu = option.menu
	option.delete()
	return redirect('menu:view', menu_id=menu.id)		