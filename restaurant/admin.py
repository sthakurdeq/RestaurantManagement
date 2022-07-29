from django.contrib import admin
from .models import Restaurant, Ratings, Item, Menu
# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Ratings)
admin.site.register(Item)
admin.site.register(Menu)
