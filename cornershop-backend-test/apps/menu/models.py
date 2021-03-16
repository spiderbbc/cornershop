import uuid
from datetime import datetime, time
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Menu(models.Model):
	"""Models Menu"""
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

	def is_can_be_ordered(self):
		"""is_can_be_ordered return boolean if the current time is greater than 11 AM CLT"""
		today_date = datetime.now()
		today_time = time(today_date.hour, today_date.minute, today_date.second)
		return  True if today_time.hour <= 10 and today_time.minute <= 60 else False

	def is_today_menu(self):
		"""is_today_menu return boolean if the menu is create today based with start_on property"""
		date_of_today = datetime.today().date()
		return  True if self.start_on == date_of_today  else False	

	def get_template_menu(self):
		"""get_template_menu return string template for reminder slack"""
		template = ''
		if self.options.count():
			url = '<http://127.0.0.1:8000/menu/%s>' % self.uuid
			template += url
			template += "\n\n Hello! I share with you today's menu :) \n\n"
			for index, option in enumerate(self.options.all()):
				template += "%s Option: %s \n" % (index + 1,option.description) 	
			template += "\n\nHave a nice day!\n\n"
		return template			
		
class Option(models.Model):
	"""Models Options"""
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