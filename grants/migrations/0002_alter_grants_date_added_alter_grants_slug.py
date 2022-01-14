# Generated by Django 4.0.1 on 2022-01-12 15:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('grants', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grants',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2022, 1, 12, 15, 8, 17, 310442, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='grants',
            name='slug',
            field=models.SlugField(max_length=250, unique_for_date='date_added'),
        ),
    ]
