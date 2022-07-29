from restaurant.models import Ratings, Restaurant, Item, Menu
from rest_framework import serializers

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'state', 'city', 'country', 'street']

class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super().__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

class MenuSerializer(DynamicFieldsModelSerializer):
    items = serializers.SerializerMethodField()
    class Meta:
        model = Menu
        fields = ['id', 'restaurants', 'day', 'vote', "item", 'items']

    def get_items(self, obj):
        return obj.item.all().values("id", "name")


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'type', 'description']

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ratings
        fields = ['menu','timestamp','user','rating'] 