from datetime import date
from django import forms
from django.forms.fields import DateField
from .models import Menu,Option

class MenuCreateForm(forms.ModelForm):
	"""MenuCreateForm: create and update form to Menu"""
	def clean_start_on(self):
		start_on = self.cleaned_data['start_on']
		today = date.today()
		if start_on < today:
			raise forms.ValidationError("The start date must be greater than today's date. {}".format(today.strftime("%d-%m-%y")))
		return start_on
	class Meta:
		model = Menu
		fields = ['name','start_on']	
		widgets = {
		'start_on': forms.DateInput(format=('%Y-%m-%d'),
			attrs = {'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
		}

class OptionCreateForm(forms.ModelForm):
	"""OptionCreateForm: create and update form to Order"""
	description = forms.CharField(max_length=100)
	class Meta:
		model = Option
		fields = ['description']

