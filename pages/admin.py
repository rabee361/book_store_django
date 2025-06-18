from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import *

@admin.register(Book)
class CustomAdminClass(ModelAdmin):
    pass
