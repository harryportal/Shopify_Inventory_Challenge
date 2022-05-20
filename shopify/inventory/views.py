from django.shortcuts import render
from .models import Inventory, Item
from django.views import generic
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def create(request):
    """ create a new inventory product """
    if request.method == 'POST':
        inventory_name = request.POST['name']
        inventory = Inventory.objects.filter(name=inventory_name).first()
        if inventory is None:
            new_inventory = Inventory(name=inventory_name)
            new_inventory.save()
            return HttpResponseRedirect(reverse('inventory:inventories'))
        else:
            error = 'Inventory name exist!, Please input a new inventory'
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
    try:
        inventory = Inventory.objects.get(pk=inventory_id)
    except(KeyError, Inventory.DoesNotExist):
        error_message = 'Inventory does not exist'
        inventories = Inventory.objects.all()
        context = {'error': error_message, 'inventories': inventories}
        return render(request, 'inventory/home.html', context)
    else:
        inventory_items = inventory.item_set.filter(deleted=False).all()
        context = {'inventory': inventory, 'inventory_items': inventory_items}
        return render(request, 'inventory/veiw_inventory.html', context)


def create_item(request, inventory_id):
    """ create a new inventory product """
    try:
        inventory = Inventory.objects.get(pk=inventory_id)
    except(KeyError, Inventory.DoesNotExist):
        error_message = 'Inventory does not exist'
        inventories = Inventory.objects.all()
        context = {'error': error_message, 'inventories': inventories}
        return render(request, 'inventory/home.html', context)
    if request.method == 'POST':
        # check if item is in database
        item = Item.objects.filter(name=request.POST['name']).first()
        if item is None:
            add = request.POST
            new_item = Item(name=add['name'], quantity=add['quantity'],
                            sales=add['sales'], price=add['price'], inventory_id=inventory.id,
                            in_stock=add.get('in_stock', False))
            new_item.save()
            return HttpResponseRedirect(reverse('inventory:view_inventory', args=(inventory.id,)))
        else:  # item exists
            error_message = 'Cannot add item with duplicate Name!'
            context = {'error': error_message, 'inventory': inventory}
            return render(request, 'inventory/add_item.html', context)
    else:
        return render(request, 'inventory/add_item.html', {'inventory': inventory})


def delete_item(request, item_id):
    try:
        item = Item.objects.get(pk=item_id)
    except(KeyError, Item.DoesNotExist):
        error_message = 'Item does not exist'
        inventories = Inventory.objects.all()
        context = {'error': error_message, 'inventories': inventories}
        return render(request, 'inventory/home.html', context)
    inventory = Inventory.objects.get(pk=item.inventory_id)
    if request.method == 'POST':
        item.deleted = True
        item.deletion_comment = request.POST['comment']
        item.save()
        return HttpResponseRedirect(reverse('inventory:view_inventory', args=(inventory.id,)))
    else:
        return render(request, 'inventory/delete_item.html', {'item': item, 'inventory_name': inventory.name})


def update_item(request, item_id):
    try:
        item = Item.objects.get(pk=item_id)
    except(KeyError, Item.DoesNotExist):
        error_message = 'Item does not exist'
        inventories = Inventory.objects.all()
        context = {'error': error_message, 'inventories': inventories}
        return render(request, 'inventory/home.html', context)
    if request.method == 'POST':
        add = request.POST
        try:
            item = Item.objects.filter(name=request.POST['name']).first()
        except(KeyError, Item.DoesNotExist):
            item.name = add['name']
            item.quantity = add['quantity']
            item.sales = add['sales']
            item.in_stock = add.get('in_stock', False)
            item.price = add['price']
            item.save()
            return HttpResponseRedirect(reverse('inventory:view_inventory', args=(item.inventory_id,)))
        if add['name'] == item.name:
            item.name = add['name']
            item.quantity = add['quantity']
            item.sales = add['sales']
            item.in_stock = add.get('in_stock', False)
            item.price = add['price']
            item.save()
            return HttpResponseRedirect(reverse('inventory:view_inventory', args=(item.inventory_id,)))
        else:
            error_message = 'Cannot add item with duplicate Name!'
            context = {'error': error_message, 'item': item}
            return render(request, 'inventory/edit_item.html', context)
    else:
        return render(request, 'inventory/edit_item.html', {'item': item})


def view_deleteditems(request, inventory_id):
    try:
        inventory = Inventory.objects.get(pk=inventory_id)
    except(KeyError, Inventory.DoesNotExist):
        error_message = 'Inventory does not exist'
        inventories = Inventory.objects.all()
        context = {'error': error_message, 'inventories': inventories}
        return render(request, 'inventory/home.html', context)
    else:
        inventory_items = inventory.item_set.filter(deleted=True).all()
        context = {'inventory': inventory, 'inventory_items': inventory_items}
        return render(request, 'inventory/deleted_items.html', context)



def undo_deletion(request, item_id):
    try:
        item = Item.objects.get(pk=item_id)
    except(KeyError, Item.DoesNotExist):
        error_message = 'Item does not exist'
        inventories = Inventory.objects.all()
        context = {'error': error_message, 'inventories': inventories}
        return render(request, 'inventory/home.html', context)
    else:
        inventory = Inventory.objects.get(pk=item.inventory_id)
        item.deleted = False
        item.save()
        return HttpResponseRedirect(reverse('inventory:view_inventory', args=(inventory.id,)))
