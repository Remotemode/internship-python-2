from django.urls import path

from .views import *



urlpatterns = [
    path('index', index),
    path('sort', sort),
    path('dishing', get_dish_by_dish),
    path('insert', insert),
    path('', home)
]