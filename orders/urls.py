from django.urls import path
from . import views

urlpatterns = [
    path('payments/', views.payments, name='payments'),
    path('place_order/', views.place_order, name='place_order'),
    path('order_complete/<str:order_number>/<str:transID>/', views.order_complete, name='order_complete'),
    path('cashondelivery/', views.cashondelivery, name='cashondelivery'),
]
    