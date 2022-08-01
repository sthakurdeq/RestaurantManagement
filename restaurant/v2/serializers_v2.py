from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from restaurant.models import Ratings


class RatingV2Serializer(serializers.ModelSerializer):
    """
    Rating serializer with fields to control displayed fields.
    fields: menu, timestamp, user, rating
    """

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    menu = serializers.DictField(
        child=serializers.IntegerField(min_value=1, max_value=3)
    )

    class Meta:
        model = Ratings
        fields = ["id", "menu", "user"]
