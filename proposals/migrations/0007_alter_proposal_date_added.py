# Generated by Django 3.2.8 on 2022-02-13 13:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0006_alter_proposal_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposal',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2022, 2, 13, 13, 51, 5, 554705, tzinfo=utc), verbose_name='recorded date'),
        ),
    ]
