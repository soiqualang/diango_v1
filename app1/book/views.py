# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import Http404

from django.shortcuts import render
from .models import Category, Book

# Create your views here.
def index(request):
    type_objs = Type.objects.filter(active__exact=True)
    context = {
        'type_objs': type_objs,
    }
    return render(request, "cats.html", context)
    
def product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        raise Http404("Product does not exist")
    return render(request, 'book_detail.html', {'product': product})