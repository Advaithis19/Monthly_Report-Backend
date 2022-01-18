# Generated by Django 3.2.8 on 2022-01-17 11:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('grants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='grants',
            name='CO_PI',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='grants_coprinvestigated', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='grants',
            name='PI',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='grants_prinvestigated', to=settings.AUTH_USER_MODEL),
        ),
    ]
