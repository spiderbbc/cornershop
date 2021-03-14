from django.urls import path

from . import views

urlpatterns = [
    # ex: /menu/
    path('<uuid:menu_uuid>', views.order_create, name='order_create'),
    path('order/view/<int:order_id>/', views.order_view, name='order_view'), 
]