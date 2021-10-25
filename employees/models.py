from django.db import models

# Create your models here.
class Employee(models.Model):

   eid = models.CharField(max_length=100)
   name = models.CharField(max_length=100)
   age = models.IntegerField()
   salary = models.IntegerField()
   address = models.TextField()



   def __str__(self):
      return self.eid + ' ' + self.name

