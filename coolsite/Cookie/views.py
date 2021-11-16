from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .models import Dish


# Create your views here.

def index(request):  # HttpRequest
    posts = Dish.objects.all().explain()
    posts.save()
    print(posts.explain())
    return HttpResponse(" ")


def get_dish_by_dish(request, name):
    posts = Dish.objects.filter(name=name)
    print(posts.explain())
    return HttpResponse("get_ingredients_by_dish")


def filter_by_date(request, data_start, data_finish):
    posts = Dish.objects.all().filter(data_start, data_finish)
    print(posts.explain())
    return HttpResponse("sort")


def sort(request):  # HttpRequest
    order_by = request.GET.get('order_by', 'price')
    posts = Dish.objects.all().order_by(order_by).explain()
    print(posts.explain())
    return HttpResponse("sort")


def insert(request, name, quantity):
    dish = Dish.objects.create(name=name)
    Dish.authors.add(dish)
    Dish.save()
    print(dish.explain())

