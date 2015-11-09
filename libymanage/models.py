from django.db import models

# Create your models here.
class Author(models.Model):
    authorid = models.CharField(max_length=30, primary_key = True)
    name = models.CharField(max_length=30)
    age = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    
class Book(models.Model):
     ISBN = models.CharField(max_length=30, primary_key = True)
     title = models.CharField(max_length=30)
     authorid = models.ForeignKey(Author)
     publisher = models.CharField(max_length=30)
     publishdate = models.CharField(max_length=30)
     price = models.CharField(max_length=30)