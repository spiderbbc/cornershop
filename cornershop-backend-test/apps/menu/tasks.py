from celery import task
from .models import Menu


#@task 
def reminders_menu(menu_id):
	"""Task to send an slack reminders when an menu have options to send."""
	menu = Menu.objects.filter(pk=menu_id)
	print(menu)
	#return message_slack	