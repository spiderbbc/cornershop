# Welcome to backend_test’s documentation



1. ##### Definitions and requirements specifications

   1. **general definition of software**:  a system that allows the employer to send their employees the menu of the day by means of a reminder on the Slack platform
   2. **project requirement specifications**:
      1. the process of sending the reminders has to be asynchronous using the celery library
      2. the employer can create a menu for a specific date.
      3. the employer can send a Slack reminder with today's menu to all chilean employees.
      4. the employees should be able to Choose their preferred meal (until 11 AM CLT)
      5. Specify customizations (e.g. no tomatoes in the salad).
      6. the employer should be the only user to be able to see what the Cornershop employees have requested, and to create and edit today's menu.
      7. The employees should be able to specify what they want for lunch but they shouldn't be able to see what others have requested.
      8. The slack reminders must contain an URL to today's menu with the following pattern  https://nora.cornershop.io/menu/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx (an UUID)

2. ##### entity relationship diagram

   ![](/home/xavier/cornershop/cornershop/src/backend-test-master/cornershop-backend-test/docs/cornershop.png)

