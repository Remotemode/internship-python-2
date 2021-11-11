from flask import Flask
import sqlite3
import Dish as D
import Ingredients as I

dish = D.Dish()
dish.get_all()
dish.insert_dish('FE66R', 'FD', 34)
dish.update_dish("FEE66R", 44)
dish.delete_dish(5)
dish.get_ingredients_by_dish("FE66R")
dish.price_ingredients_for_dish(2)

ingredients = I.Ingredients()
ingredients.get_all_ingredients()
ingredients.insert_ingredients("tomat", 2, 44)
ingredients.update_ingredients("SSS", 25)
ingredients.delete_ingredients(3)
