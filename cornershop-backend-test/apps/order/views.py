from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from apps.menu.models import Menu,Option
from .models import Order
from .forms import OrderCreateForm
# Create your views here.
def order_create(request,menu_uuid):
	menu = get_object_or_404(Menu, uuid = menu_uuid)
	form = OrderCreateForm()
	form.fields['option'].choices = [(o.id, str(o)) for o in Option.objects.filter(menu_id=menu.id)]
	if request.method == 'POST':
		form = OrderCreateForm(request.POST)
		if form.is_valid():
			order = form.save()
			return redirect('order:order_view', order_id=order.id)
				
	return render(request,'order/order.html',{'menu':menu,'form':form})
@login_required
def order_list(request):
	#obj = Menu.objects.filter(user_id = request.user.id)
	user_id = request.user.id
	orders = Order.objects.filter(option__menu__user_id = user_id)
	return render(request,'order/list.html',{'orders':orders})
@login_required
def order_view(request,order_id):
	order = get_object_or_404(Order,pk= order_id)
	return render(request,'order/view.html',{'order':order})	