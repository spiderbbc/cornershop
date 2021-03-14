from django.urls import path

from . import views

urlpatterns = [
    # ex: /menu/
    path('', views.menu_list, name='index'),
    path('create/', views.menu_create, name='create'),
    path('view/<int:menu_id>/', views.menu_view, name='view'),
    path('update/<int:menu_id>/', views.menu_update, name='update'),
]