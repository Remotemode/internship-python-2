from django.urls import path

from .views import *



urlpatterns = [
    path('', index),
    # path('dish', get_dish_by_dish(4))
]