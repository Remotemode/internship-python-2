from django.urls import path

from .views import *



urlpatterns = [
    path('coo', index),
    path('sort', sort),
    path('dishing', get_dish_by_dish),
    path('dish', insert)
]