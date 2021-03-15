from django.urls import path

from . import views

urlpatterns = [
    # ex: /
    path('', views.menu_list, name='index'),
    path('create/', views.menu_create, name='create'),
    path('view/<int:menu_id>/', views.menu_view, name='view'),
    path('update/<int:menu_id>/', views.menu_update, name='update'),
    path('reminders/<int:menu_id>/', views.menu_reminders, name='reminders'),
    # ex: /option
    path('option/create/<int:menu_id>/', views.option_create, name='option_create'),
    path('option/update/<int:option_id>/', views.option_update, name='option_update'),
    path('option/delete/<int:option_id>/', views.option_delete, name='option_delete'),

]