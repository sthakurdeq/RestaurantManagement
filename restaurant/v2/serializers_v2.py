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
    vote_value = serializers.IntegerField(source="vote")

    class Meta:
        model = Ratings
        fields = ["id", "menu", "user", "vote"]

    def validate(self, data):
        # breakpoint()
        data = dict(data)
        if len(data["menu"].values()) >= 3:
            raise ValidationError({"menu": "Cannot rate more than 3 menus"})

        if len(data["menu"].values()) != len(set(data["menu"].values())):
            raise ValidationError({"menu": "Multiple menus cannot have same rating"})
