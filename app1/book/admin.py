# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Category, Book

# Register your models here.

class CategoryModelAdmin(admin.ModelAdmin):
    #list_filter = ('active',)
    list_display = ['name']

class BookModelAdmin(admin.ModelAdmin):
    #readonly_fields = ('image_tag',)
    list_display = ['name', 'price', 'category', 'author_name']

admin.site.register(Category, CategoryModelAdmin)
admin.site.register(Book, BookModelAdmin)