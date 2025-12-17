from django.contrib import admin

# Register your models here.

from .models import GolfItem

admin.site.register(GolfItem)