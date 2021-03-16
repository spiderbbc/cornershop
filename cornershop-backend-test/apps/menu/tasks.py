from celery import task
from backend_test.utils.slack import users_list,reminders_add
from .models import Menu


@task(trail=True) 
def reminders_menu(menu_id):
	"""Task to send an slack reminders when an menu have options to send."""
	messages = []
	employees_slack = users_list()
	if len(employees_slack):
		menu = Menu.objects.get(pk=menu_id)
		if not menu.options.count():
			messages.append("El menu debe de tener opciones registradas para enviar los recordatorios")
			return messages
		
		time_reminder = "in 5 seconds" if menu.is_today_menu()  else menu.start_on.strftime('%s')		
		text = menu.get_template_menu()
		reminders_status = reminders_add(employees_slack,text,time_reminder)
		messages = reminders_status
	else:	
		messages.append("No se encontraron empleados en slack para enviar el recordatorio")
	return messages