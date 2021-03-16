from django import forms
from apps.menu.models import Option
from .models import Order

class OrderCreateForm(forms.ModelForm):
	"""OrderCreateForm: create and update form to Orders"""
	name = forms.CharField(max_length=100)
	rut = forms.CharField(max_length=12)
	customatizacion = forms.CharField(max_length=100)
	
	class Meta:
		model = Order
		fields = ['name','rut','option','customatizacion']
	

