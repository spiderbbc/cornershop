import uuid
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Menu(models.Model):
	"""docstring for Menu"""
	user = models.ForeignKey(User, related_name='users',on_delete=models.CASCADE)
	uuid = models.UUIDField(default=uuid.uuid4,db_index=True, editable=False, unique=True)
	name = models.CharField(max_length=200, db_index=True)
	send = models.BooleanField(default=False)
	start_on = models.DateField(auto_now=False, auto_now_add=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['name']
		verbose_name = 'menu'
		verbose_name_plural = 'menus'
		indexes = [
			models.Index(fields=['id', 'uuid']),
		]

	
	def __str__(self):
		return '{}: {}'.format(self.name,self.start_on)
		
class Option(models.Model):
	"""docstring for Option"""
	menu = models.ForeignKey(Menu, related_name='options',on_delete=models.CASCADE)
	description = models.CharField(max_length=200)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-created']
		verbose_name = 'option'
		verbose_name_plural = 'options'

	def __str__(self):
		return '{}'.format(self.description)	