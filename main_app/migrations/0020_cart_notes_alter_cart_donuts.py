# Generated by Django 4.0.2 on 2022-02-15 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0019_alter_cart_donuts_alter_itemcart_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='notes',
            field=models.TextField(default='hello'),
            preserve_default=False,
        ),
        # migrations.AlterField(
        #     model_name='cart',
        #     name='donuts',
        #     field=models.ManyToManyField(through='main_app.ItemCart', to='main_app.Donut'),
        # ),
    ]
