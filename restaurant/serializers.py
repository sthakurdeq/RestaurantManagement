from restaurant.models import Restaurant, Item, Menu
from rest_framework import serializers

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['name', 'state', 'city', 'country', 'street']


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['restaurant_name', 'day', 'vote', 'item']


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['name', 'type', 'description']
