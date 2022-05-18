from django.urls import path
from .views import ListView


app_name = 'inventory'
urlpatterns =[
    path('', ListView.as_view(), name='inventory_list')
]