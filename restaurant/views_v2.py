from datetime import datetime

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from restaurant.models import Ratings
from restaurant.serializers_v2 import RatingV2Serializer
from restaurant.views import RatingViewSet


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
        serializer = RatingV2Serializer(data=request.data, context={"request": request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
