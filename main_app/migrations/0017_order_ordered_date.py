# Generated by Django 4.0.2 on 2022-02-14 21:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0016_alter_order_delivery_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='ordered_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 14, 21, 42, 15, 400546, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
