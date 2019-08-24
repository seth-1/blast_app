from django.contrib import admin

from .models import BlastQuery, BlastResult
# Register your models here.

admin.site.register(BlastQuery)
admin.site.register(BlastResult)
