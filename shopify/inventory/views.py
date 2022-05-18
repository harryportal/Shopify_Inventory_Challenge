from django.shortcuts import render
from .models import Inventory
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


class ViewInventory_Items(generic.DetailView):
    """ returns a list of inventory items """
    model = Inventory
    template_name = 'inventory/view_inventory.html'
    context_object_name = 'inventories'



def delete(request, inventory_id):
    try:
        inventory = Inventory.objects.get(pk=inventory_id)
    except(KeyError, Inventory.DoesNotExist):
        error_message = 'Invalid operation, Inventory item does not exist!'
        return render(request, 'inventory/home.html', {'error_message': error_message})
    else:
        inventory.delete()
        return HttpResponseRedirect(reverse('inventory:inventory_list'))


def update(request, inventory_id):
    try:
        inventory = Inventory.objects.get(pk=inventory_id)
    except(KeyError, Inventory.DoesNotExist):
        error_message = 'Invalid operation, Inventory item does not exist!'
        return render(request, 'inventory/home.html', {'error_message': error_message})
    else:
        new_inventory_name = request.POST['name']
        new_inventory_price = request.POST['price']
        inventory.name = new_inventory_name
        inventory.price = new_inventory_price
        inventory.save()
        return HttpResponseRedirect(reverse('inventory:inventory_list'))
