from django.db import models


class Composition(models.Model):
    id_ingredienta = models.IntegerField(blank=True, null=True)
    id_dish = models.IntegerField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Composition'


class Dish(models.Model):
    #id_dish = models.IntegerField()
    name = models.TextField(blank=True, null=True, default='')
    quantity = models.TextField(blank=True, null=True, default='')
    price = models.IntegerField(blank=True, null=True, default='')

    class Meta:
        managed = True
        db_table = 'Dish'


class Ingredients(models.Model):
    # id_ingredient = models.AutoField()
    name = models.TextField()
    count = models.IntegerField(db_column='Count')  # Field name made lowercase.
    price = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Ingredients'
