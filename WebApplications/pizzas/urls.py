"""Defines URL patterns for learning_logs"""
from django.urls import path
from . import views
app_name = 'pizzas'
urlpatterns = [
  #   Home page
  path('', views.index, name = "index"),
  #   Show all pizzas
  path('pizzas/', views.pizzas, name = "pizzas"),
  #   Detail page for a single topic
  path('pizzas/<int:pizza_id>/', views.pizza, name = "pizza"),
]
