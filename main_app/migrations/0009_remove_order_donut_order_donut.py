# Generated by Django 4.0.2 on 2022-02-12 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_order_donut'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='donut',
        ),
        migrations.AddField(
            model_name='order',
            name='donut',
            field=models.ManyToManyField(to='main_app.Donut'),
        ),
    ]
