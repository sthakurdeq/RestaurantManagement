from django.contrib import admin
from .models import Ratings, Restaurant, Item, Menu

# Register your models here.
admin.site.register(Ratings)
admin.site.register(Restaurant)
admin.site.register(Item)
admin.site.register(Menu)