from django.urls import path
from .views import Inventories, create, ViewInventory_Items

app_name = 'inventory'

urlpatterns =[
    path('', Inventories.as_view(), name='inventories'),
    path('add/', create, name='add_inventory'),
    path('view/<int:pk>', ViewInventory_Items.as_view(), name='view_inventory')
]