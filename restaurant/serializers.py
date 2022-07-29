from restaurant.models import Ratings, Restaurant, Item, Menu
from rest_framework import serializers

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'state', 'city', 'country', 'street']


class MenuSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()
    class Meta:
        model = Menu
        fields = ['id', 'restaurants', 'day', 'vote', 'items']

    def get_items(self, obj):
        # breakpoint()
        return obj.item.all().values("id", "name")



class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'type', 'description']

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ratings
        fields = ['menu','timestamp','user','rating'] 