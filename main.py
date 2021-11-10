from flask import Flask
import sqlite3
import Dish as D

dish = D.Dish()
dish.get_all()
dish.insert_dish('FE66R', 'FD', 34)
dish.update_dish("FEE66R", 44)
dish.delete_dish(5)
