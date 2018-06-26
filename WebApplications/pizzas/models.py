from django.db import models

# Create your models here.
class Pizza(models.Model) :
  """A pizza test"""
  name = models.CharField(max_length = 200)
  date_added = models.DateTimeField(auto_now_add = True)
  def __str__(self) :
    """Return a string representation of the Pizza"""
    return self.name

class Topping(models.Model) :
  """Something specific for the pizza"""
  pizza = models.ForeignKey(Pizza, on_delete = models.CASCADE)
  name = models.TextField()
  date_added = models.DateTimeField(auto_now_add = True)
  class Meta :
    verbose_name_plural = "topping"
  def __str__(self) :
    """return a string representation of the topping"""
    return self.name
