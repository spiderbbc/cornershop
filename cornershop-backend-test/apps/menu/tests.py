import uuid
from datetime import date
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Menu,Option
from .forms import MenuCreateForm

class MenuTestCase(TestCase):
    def setUp(self):
    	self.user = User.objects.create(username='user1')
    	self.menu = Menu.objects.create(user =self.user,name="Menu del dia",start_on= date.today())
    	self.option = Option.objects.create(menu=self.menu,description="Corn pie, Salad and Dessert")

    def test_is_can_be_ordered(self):
        """Menu can be order"""
        self.assertEqual(self.menu.is_can_be_ordered(),False)

    def test_is_today_menu(self):
    	"""Menu is create today"""
    	self.assertEqual(self.menu.is_today_menu(),True) 

    def test_template_menu(self):
    	"""Menu template slack reminder"""
    	template = "<http://127.0.0.1:8000/menu/%s>\n\n Hello! I share with you today's menu :) "\
    	"\n\n1 Option: Corn pie, Salad and Dessert \n\n\nHave a nice day!\n\n" % self.menu.uuid
    	self.assertEqual(self.menu.get_template_menu(),template) 	
    	  
    def tearDown(self):
    	"""Delete data test"""
    	self.user.delete()
    	self.menu.delete()
    	self.option.delete()  

class MenuCreateFormTestCase(TestCase):

  	def test_clean_start_on_error_raise(self):
  		form = MenuCreateForm(data={"name": "Menu test","start_on":"2021-12-12"})
  		today = date.today()
  		error = "The start date must be greater than today's date. {}".format(today.strftime("%d-%m-%y"))
  		self.assertEqual(form.errors["start_on"], [error])	
  		    	  
