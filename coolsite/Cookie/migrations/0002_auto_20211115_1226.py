# Generated by Django 3.2.9 on 2021-11-15 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cookie', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('count', models.IntegerField(db_column='Count')),
                ('price', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Ingredients',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Composition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_ingredienta', models.IntegerField(blank=True, null=True)),
                ('id_dish', models.IntegerField(blank=True, null=True)),
                ('count', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Composition',
                'managed': True,
            },
        ),
        migrations.AlterModelOptions(
            name='dish',
            options={'managed': True},
        ),
        migrations.AlterField(
            model_name='dish',
            name='name',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='dish',
            name='price',
            field=models.IntegerField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='dish',
            name='quantity',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterModelTable(
            name='dish',
            table='Dish',
        ),
    ]
