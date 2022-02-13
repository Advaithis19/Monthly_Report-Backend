# Generated by Django 3.2.8 on 2022-02-13 08:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activity',
            options={'ordering': ('-date_added',), 'verbose_name_plural': 'other activities'},
        ),
        migrations.AlterField(
            model_name='activity',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2022, 2, 13, 8, 18, 47, 591557, tzinfo=utc), verbose_name='recorded date'),
        ),
    ]