from datetime import datetime

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from restaurant.models import Ratings
from restaurant.v1.serializers import RatingSerializer
from restaurant.v1.views import RatingViewSet
from restaurant.v2.serializers_v2 import RatingV2Serializer


@method_decorator(csrf_exempt, name="dispatch")
class RatingV2ViewSet(RatingViewSet):
    """
    Rating View Accept GET, POST
    return fields as per the RatingSerializer
    """

    http_method_names = ["get", "post"]
    authentication_classes = [TokenAuthentication]
    queryset = Ratings.objects.all()
    serializer_class = RatingV2Serializer

    def create(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        today = datetime.today()
        user_rating = Ratings.objects.filter(
            user=request.user,
            created_at__year=today.year,
            created_at__month=today.month,
            created_at__day=today.day,
        )
        if len(user_rating) >= 1:
            raise ValidationError({"rating": "user can rate menu once a day."})
        menus = request.data["menu"]
        if len(menus) >= 3:
            raise ValidationError({"menu": "Cannot rate more than 3 menus"})

        if len(menus.values()) != len(set(menus.values())):
            raise ValidationError({"menu": "Multiple menus cannot have same rating"})

        for menu in menus:
            data = {"user": request.user, "menu": menu, "vote_value": menus[menu]}

            serializer = RatingSerializer(data=data, context={"request": request})
            if serializer.is_valid(raise_exception=True):
                serializer.save()
        return Response(
            {"Result": "Thanks for menu voting"}, status=status.HTTP_201_CREATED
        )
