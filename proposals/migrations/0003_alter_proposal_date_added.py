# Generated by Django 4.0.1 on 2022-02-11 11:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0002_alter_proposal_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposal',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2022, 2, 11, 11, 6, 53, 311058, tzinfo=utc), verbose_name='recorded date'),
        ),
    ]
