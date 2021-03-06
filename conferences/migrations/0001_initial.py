# Generated by Django 4.0.1 on 2022-02-13 15:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='title of publication')),
                ('conference', models.CharField(max_length=100, verbose_name='conference')),
                ('volume', models.IntegerField(verbose_name='volume #')),
                ('issue', models.IntegerField(verbose_name='issue #')),
                ('n_page', models.IntegerField(verbose_name='page #')),
                ('nat_int', models.CharField(choices=[('NAT', 'National'), ('INT', 'International')], max_length=3, null=True, verbose_name='national/international')),
                ('date_added', models.DateField(default=datetime.datetime(2022, 2, 13, 15, 24, 49, 778826, tzinfo=utc), verbose_name='recorded date')),
            ],
            options={
                'db_table': 'conference',
                'ordering': ('-date_added',),
            },
        ),
    ]
