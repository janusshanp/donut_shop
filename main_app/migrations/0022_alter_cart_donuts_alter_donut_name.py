# Generated by Django 4.0.2 on 2022-02-16 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0021_alter_cart_donuts_alter_cart_notes'),
    ]

    operations = [
        # migrations.AlterField(
        #     model_name='cart',
        #     name='donuts',
        #     field=models.ManyToManyField(through='main_app.ItemCart', to='main_app.Donut'),
        # ),
        migrations.AlterField(
            model_name='donut',
            name='name',
            field=models.CharField(max_length=40),
        ),
    ]