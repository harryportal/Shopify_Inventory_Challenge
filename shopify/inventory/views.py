from django.shortcuts import render
from .models import Inventory
from django.views import generic

def create(request):
    """ create a new inventory product """


class ListView(generic.ListView):
    model = Inventory
    template_name = 'polls/home.html'
    context_object_name = 'inventory_list'

    def get_queryset(self):
        return Inventory.objects.all()



