"""Defines URL patterns for learning_logs"""
from django.urls import path
# from . import views as learning_logs_views
#from learning_logs.views import index
from . import views
app_name = 'learning_logs'
urlpatterns = [
  #   Home page
  # url(r'^$', views.index, name = "index")
  path('', views.index, name = "index"),
  # path(r'^$', index, name = "index")
  #   Show all topics
   path('topics/', views.topics, name = "topics"),
]
