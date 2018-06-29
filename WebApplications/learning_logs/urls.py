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
  #   Detail page for a single topic
  path('topics/<int:topic_id>/', views.topic, name = "topic"),
  #   Page for adding a new topic
  path('new_topic/', views.new_topic, name = 'new_topic'),
  #   Page for adding a new entry
  path('new_entry/<int:topic_id>/', views.new_entry, name = 'new_entry'),
]
