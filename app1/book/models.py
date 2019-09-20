# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.conf import settings
import django.utils.safestring as safestring

# Create your models here.

#Category model có field name
class Category(models.Model):
   name = models.CharField(max_length=200)
   def __str__(self):
     return self.name

#Book model có field name, price, category, author_name
class Book(models.Model):
   name = models.CharField(max_length=200)
   price = models.IntegerField(default=0)
   category = models.ForeignKey(Category, on_delete=models.CASCADE)
   author_name = models.CharField(max_length=200)
   def __str__(self):
     return self.name