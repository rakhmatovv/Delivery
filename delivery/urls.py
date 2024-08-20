from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('delivery/', delivery, name= 'delivery'),
    path('delivery_list/', delivery_list, name='delivery_list'),
]