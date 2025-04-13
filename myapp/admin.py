# myapp/admin.py
from django.contrib import admin
from .models import Item, Order  # example models

admin.site.register(Item)
admin.site.register(Order)
