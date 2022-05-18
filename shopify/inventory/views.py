from django.shortcuts import render
from .models import Inventory, Item
from django.views import generic
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render


def create(request):
    """ create a new inventory product """
    if request.method == 'POST':
        inventory_name = request.POST['name']
        if inventory_name:
            new_inventory = Inventory(name=inventory_name)
            new_inventory.save()
            return HttpResponseRedirect(reverse('inventory:inventories'))
        else:
            error = 'Please input a valid name'
            return render(request, 'inventory/add_inventory.html', {'error_message': error})
    else:
        return render(request, 'inventory/add_inventory.html')


class Inventories(generic.ListView):
    """ returns a list of inventory items """
    model = Inventory
    template_name = 'inventory/home.html'
    context_object_name = 'inventories'

    def get_queryset(self):
        return Inventory.objects.all()


def ViewInventory_Items(request, inventory_id):
    inventory = Inventory.objects.get(pk=inventory_id)
    inventory_items = inventory.item_set.filter(deleted=False).all()
    context = {'inventory':inventory, 'inventory_items':inventory_items}
    return render(request, 'inventory/veiw_inventory.html', context)



def create_item(request, inventory_id):
    """ create a new inventory product """
    try:
        inventory = Inventory.objects.get(pk=inventory_id)
    except(KeyError, Inventory.DoesNotExist):
        return HttpResponseRedirect(reverse('inventory:inventories'))
    if request.method == 'POST':
        add = request.POST
        new_item = Item(name=add['name'], quantity=add['quantity'],
                        sales=add['sales'], in_stock=add['in_stock'],
                        price=add['price'], inventory_id=inventory.id)
        new_item.save()
        return HttpResponseRedirect(reverse('inventory:view_inventory', args=(inventory.id,)))
    else:
        return render(request, 'inventory/add_item.html', {'inventory': inventory})


def delete_item(request, item_id):
    try:
        item = Item.objects.get(pk=item_id)
    except(KeyError, Inventory.DoesNotExist):
        return HttpResponseRedirect(reverse('inventory:inventories'))
    inventory = Inventory.objects.get(pk=item.inventory_id)
    if request.method == 'POST':
        item.deleted = True
        item.save()
        return HttpResponseRedirect(reverse('inventory:view_inventory', args=(inventory.id,)))
    else:
        return render(request, 'inventory/delete_item.html', {'item': item, 'inventory_name':inventory.name})


def update_item(request, item_id):
    try:
        item = Item.objects.get(pk=item_id)
    except(KeyError, Inventory.DoesNotExist):
        return HttpResponseRedirect(reverse('inventory:inventories'))
    if request.method == 'POST':
        add = request.POST
        item.name = add['name']
        item.quantity = add['quantity']
        item.sales = add['sales']
        item.in_stock = add['in_stock']
        item.price = add['price']
        item.save()
        return HttpResponseRedirect(reverse('inventory:view_inventory', args=(item.inventory_id,)))
    else:
        return render(request, 'inventory/edit_item.html', {'item':item})

def view_deleteditems(request, inventory_id):
    inventory = Inventory.objects.get(pk=inventory_id)
    inventory_items = inventory.item_set.filter(deleted=True).all()
    context = {'inventory': inventory, 'inventory_items': inventory_items}
    return render(request, 'inventory/deleted_items.html', context)

def undo_deletion(request, item_id):
    item = Item.objects.get(pk=item_id)
    inventory = Inventory.objects.get(pk=item.inventory_id)
    item.deleted = False
    item.save()
    return HttpResponseRedirect(reverse('inventory:view_inventory', args=(inventory.id,)))

