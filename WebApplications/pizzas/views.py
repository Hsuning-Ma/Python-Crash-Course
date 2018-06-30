from django.shortcuts import render
from .models import Pizza

# Create your views here.
def index(request) :
  """The home page for Pizzas"""
  return render(request, 'pizzas/index.html')
def pizzas(request) :
  """Show all the pizzas"""
  pizzas = Pizza.objects.order_by('date_added')
  context = {'pizzas': pizzas}
  return render(request, 'pizzas/pizzas.html', context)
def pizza(request, pizza_id) :
  """Show a single pizza and all its toppings"""
  pizza_ = Pizza.objects.get(id = pizza_id)
  toppings = pizza_.topping_set.order_by('-date_added')
  context = {'pizza': pizza_, 'toppings': toppings}
  return render(request, 'pizzas/pizza.html', context)

