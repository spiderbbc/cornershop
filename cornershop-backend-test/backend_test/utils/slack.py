import os
from datetime import datetime
from slack_sdk import WebClient

client = WebClient(token=os.environ['SLACK_BOT_TOKEN'])

def users_list():
	""" users_list return a list users on slack"""
	all_users = []
	new_results = True
	next_cursor = ""
	while new_results:
	    response = client.users_list(cursor = next_cursor)
	    members = response.get("members", [])
	    all_users.extend(members)
	    response_metadata = response.get("response_metadata", [])
	    next_cursor = response_metadata['next_cursor']
	    if next_cursor == '':
	    	new_results = False

	users = []
	for user in all_users:
		if user['tz'] == 'America/Santiago':
			users.append(user)	    	
	
	return users

def reminders_add(users_list,text,time_reminder):
	""" reminders_add loop the user a send reminders / messages only register for celery status"""
	messages = []
	for user in users_list:
		response = client.reminders_add(text=text,time=time_reminder,user = user['id'])
		if response['ok'] == True:
			reminder_time = int(response['reminder']['time'])
			reminder_time = datetime.utcfromtimestamp(reminder_time).strftime('%Y-%m-%d')
			messages.append("Recordatorio enviado con exito al usuario Slack %s con fecha %s" % (user['name'],reminder_time))
		else:
			messages.append("Error en Recordatorio al usario %s error: %s " % (user['name'],response['error']))
	return messages				    				    	