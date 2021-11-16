from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .models import Dish


# Create your views here.

def index(request):  # HttpRequest
    posts = Dish.objects.all().explain()
    print(posts)
    return HttpResponse()


def get_dish_by_dish(request):
    posts = Dish.objects.filter(name='fff')
    print(posts)
    return HttpResponse("get_ingredients_by_dish")


def sort(request):  # HttpRequest
    order_by = request.GET.get('order_by', 'price')
    posts = Dish.objects.all().order_by(order_by).explain()
    print(posts)
    return HttpResponse("sort", posts)


def insert(request):
    dish = Dish.objects.create(name='hgh', quantity="dff", price=0.2)
    Dish.authors.add(dish)
    Dish.save()
    print(dish.explain())
    return HttpResponse("insert")

