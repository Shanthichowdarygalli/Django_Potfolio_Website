from django.db import models

# Create your models here.
class Customer(models.Model):

   firstname = models.CharField(max_length=100)
   lastname = models.CharField(max_length=100)
   availablecolours = models.CharField(max_length=10)
   contactnumber = models.IntegerField()
   emailid = models.CharField(max_length=100)
   address = models.TextField()
   city = models.CharField(max_length=100)
   state = models.CharField(max_length=100)
   NameOfOccasion = models.CharField(max_length=100)
   weight = models.CharField(max_length=100)
   typeofcake = models.CharField(max_length=100)
   byprice = models.CharField(max_length=100)



   def __str__(self):
      return self.firstname + ' ' + self.lastname
