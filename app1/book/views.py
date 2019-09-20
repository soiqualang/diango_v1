# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import Http404

from django.shortcuts import render
from .models import Category, Book

# Create your views here.
def index(request):
    #category_objs = Type.objects.filter(active__exact=True)
    category_objs = Category.objects
    category = {
        'category_objs': category_objs,
    }
    return render(request, "cats.html", category)
    
def book(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        raise Http404("Book does not exist")
    return render(request, 'book_detail.html', {'book': book})