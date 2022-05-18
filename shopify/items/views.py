from django.shortcuts import render
from .models import Item
from django.views import generic
from django.urls import reverse
from django.http import HttpResponseRedirect



def create(request):
    """ create a new inventory product """
    inventory_name = request.POST['name']
    inventory_price = request.POST['price']
    new_inventory = Item(name=inventory_name, price=inventory_price)
    new_inventory.save()
    return HttpResponseRedirect(reverse('inventory:inventory_list'))


class ListView(generic.ListView):
    """ returns a list of inventory items """
    model = Item
    template_name = 'inventory/home.html'
    context_object_name = 'inventory_list'

    def get_queryset(self):
        return Item.objects.all()


def delete(request, inventory_id):
    try:
        inventory = Item.objects.get(pk=inventory_id)
    except(KeyError, Item.DoesNotExist):
        error_message = 'Invalid operation, Inventory item does not exist!'
        return render(request, 'inventory/home.html', {'error_message': error_message})
    else:
        inventory.delete()
        return HttpResponseRedirect(reverse('inventory:inventory_list'))


def update(request, inventory_id):
    try:
        inventory = Item.objects.get(pk=inventory_id)
    except(KeyError, Item.DoesNotExist):
        error_message = 'Invalid operation, Inventory item does not exist!'
        return render(request, 'inventory/home.html', {'error_message': error_message})
    else:
        new_inventory_name = request.POST['name']
        new_inventory_price = request.POST['price']
        inventory.name = new_inventory_name
        inventory.price = new_inventory_price
        inventory.save()
        return HttpResponseRedirect(reverse('inventory:inventory_list'))