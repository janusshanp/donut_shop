# Generated by Django 4.0.2 on 2022-02-12 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_rename_orders_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donut',
            name='order',
        ),
    ]
