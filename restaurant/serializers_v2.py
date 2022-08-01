from rest_framework import serializers

from restaurant.models import Item, Menu, Ratings, Restaurant

class RatingV2Serializer(serializers.ModelSerializer):
    """
    Rating serializer with fields to controll displayed fields
    fields: menu, timestamp, user, rating
    """

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    menu = serializers.ListField()

    class Meta:
        model = Ratings
        fields = ["id", "menu", "user", "vote", "rate"]
