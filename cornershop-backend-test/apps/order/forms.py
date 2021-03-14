from django import forms
from apps.menu.models import Option
from .models import Order

class OrderCreateForm(forms.ModelForm):
	"""docstring for OrderCreateForm"""
	name = forms.CharField(max_length=100)
	rut = forms.CharField(max_length=12)
	#option = forms.ChoiceField()
	#option = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}))
	customatizacion = forms.CharField(max_length=100)
	
	class Meta:
		model = Order
		fields = ['name','rut','option','customatizacion']
	


	# def __init__(self, *args, **kwargs):
	# 	menu_id = None
	# 	menu_id = kwargs.pop('menu_id')
	# 	kwargs.update(initial={'menu_id': menu_id})
			
	# 	super(OrderCreateForm, self).__init__(*args, **kwargs)
	# 	if 'menu_id' in kwargs:
	# 		self.fields['option'] = forms.ChoiceField(choices=[(o.id, str(o)) for o in Option.objects.filter(menu_id=menu_id)],widget=forms.Select(attrs={'class': 'form-control'}))



