# Generated by Django 4.0.2 on 2022-02-12 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_remove_order_donut_order_donut'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='rating',
            field=models.CharField(choices=[('1', 'One Star'), ('2', 'Two Star'), ('3', 'Three Star'), ('4', 'Four Star'), ('5', 'Five Star')], default='5', max_length=1),
        ),
    ]
