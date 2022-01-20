from django.contrib import admin
from . import models


@admin.register(models.Grants)
class GrantAdmin(admin.ModelAdmin):
    list_display = ('title', 'agency', 'sanc_amt',
                    'year', 'PI', 'CO_PI', 'date_added')
    prepopulated_fields = {'slug': ('title',), }