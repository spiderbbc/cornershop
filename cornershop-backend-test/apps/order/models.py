from django.db import models
from apps.menu.models import Option
# Create your models here.
class Order(models.Model):
	"""docstring for Order"""
	option = models.ForeignKey(Option, related_name='orders',on_delete=models.CASCADE)
	name = models.CharField(max_length=200, db_index=True)
	rut = models.CharField(max_length=12, db_index=True)
	customatizacion = models.CharField(max_length=200, db_index=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['name']
		verbose_name = 'order'
		verbose_name_plural = 'orders'
		indexes = [
			models.Index(fields=['id']),
		]

	
	def __str__(self):
		return '{}'.format(self.name)		