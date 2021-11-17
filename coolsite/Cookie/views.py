from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .models import Dish
from django.shortcuts import render


# Create your views here.

def index(request):  # HttpRequest
    posts = Dish.objects.all().explain()
    print("Called index")
    print(posts)
    return render(request, 'test.html')


def get_dish_by_dish(request):
    posts = Dish.objects.filter(name='fff')
    print("Called get_dish_by_dish")
    print(posts)
    return render(request, 'test.html')


def sort(request):  # HttpRequest
    order_by = request.GET.get('order_by', 'price')
    posts = Dish.objects.all().order_by(order_by).explain()
    print("Called sort")
    print(posts)
    return render(request, 'test.html')

def insert(request):
    dish = Dish.objects.create(name='hgh', quantity="dff", price=0.2)
    print("Called insert")
    return render(request, 'test.html')

def home(request):
    print('Home executed')
    sort(request)
    return render(request, 'test.html')
