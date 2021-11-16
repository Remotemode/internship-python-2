from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .models import Dish


# Create your views here.

def index(request):  # HttpRequest
    posts = Dish.objects.all().explain()
    posts.save()
    print(posts)
    return HttpResponse(" ")

#
# def get_dish_by_dish(request, name_):
#     posts = Dish(name=name_)
#     print(posts.objects())
#     return HttpResponse("get_ingredients_by_dish")


def insert_ingredients(request):
    return HttpResponse("insert_ingredients")


def sort(request):  # HttpRequest
    order_by = request.GET.get('order_by', 'price')
    posts = Dish.objects.all().order_by(order_by).explain()
    print(posts.objects())
    return HttpResponse("sort")
