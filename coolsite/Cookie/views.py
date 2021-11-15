from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .models import Dish


# Create your views here.

def index(request):  # HttpRequest
    posts = Dish.objects.all().explain()
    print(posts)
    return HttpResponse(" ")


# def get_dish_by_dish(request, id_dish=1):
#     post = {}
#     posts = Dish.objects.get(id=id_dish)
#     return HttpResponse("get_ingredients_by_dish")
#

def insert_ingredients(request):
    return HttpResponse("insert_ingredients")
