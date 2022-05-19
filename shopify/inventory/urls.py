from django.urls import path
from .views import Inventories, create, ViewInventory_Items, create_item
from .views import update_item, delete_item, view_deleteditems, undo_deletion

app_name = 'inventory'

urlpatterns =[
    path('', Inventories.as_view(), name='inventories'),
    path('add/', create, name='add_inventory'),
    path('view/<int:inventory_id>/', ViewInventory_Items, name='view_inventory'),
    path('add/item/<int:inventory_id>', create_item, name='create_item'),
    path('edit/item/<int:item_id>', update_item, name='edit_item'),
    path('delete/item/<int:item_id>', delete_item, name='delete_item'),
    path('view/deleteditems/<int:inventory_id>/', view_deleteditems, name='deleted_items'),
    path('undo_deletion/<int:item_id>', undo_deletion, name='undo_deletion')

]