from datetime import datetime

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from restaurant.models import Item, Menu, Ratings, Restaurant
from restaurant.v1.serializers import (
    ItemSerializer,
    ListRatingSerializer,
    MenuSerializer,
    RatingSerializer,
    RestaurantSerializer,
)


@method_decorator(csrf_exempt, name="dispatch")
class RestuarantViewSet(viewsets.ModelViewSet):
    """
    Restaurant View Accept GET, POST, DELETE
    return fields as per the RestaurantSerializer
    """

    queryset = Restaurant.objects.all()
    authentication_classes = [TokenAuthentication]
    serializer_class = RestaurantSerializer
    http_method_names = ["get", "post"]

    def update(self, request, pk=None):
        # returns forbidden when PUT request
        response = {"message": "Update function is not offered in this path."}
        return Response(response, status=status.HTTP_403_FORBIDDEN)

    def partial_update(self, request, pk=None):
        # returns forbidden when PATCH request
        response = {"message": "Update function is not offered in this path."}
        return Response(response, status=status.HTTP_403_FORBIDDEN)


@method_decorator(csrf_exempt, name="dispatch")
class MenuViewSet(viewsets.ModelViewSet):
    """
    Menu View Accept GET, POST, PUT, PATCH, DELETE
    return fields as per the MenuSerializer
    """

    queryset = Menu.objects.all()
    authentication_classes = [TokenAuthentication]
    serializer_class = MenuSerializer
    http_method_names = ["get", "post"]

    def create(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        data = request.data
        serializer = MenuSerializer(
            data=data, fields=["id", "restaurants", "day", "item"]
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = MenuSerializer(
            queryset, many=True, fields=["id", "restaurants", "day", "items"]
        )
        return Response(serializer.data)


@method_decorator(csrf_exempt, name="dispatch")
class TodayMenuViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Menu View Accept GET
    return todays menu based on date and day
    """

    http_method_names = ["get"]

    authentication_classes = [TokenAuthentication]
    today = datetime.today()
    day = {
        0: "MON",
        1: "TUE",
        2: "WED",
        3: "THUR",
        4: "FRI",
    }
    weekday = datetime.now().weekday()
    queryset = Menu.objects.filter(
        created_at__year=today.year,
        created_at__month=today.month,
        created_at__day=today.day,
        day=day.get(weekday),
    )
    serializer_class = MenuSerializer

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = MenuSerializer(
            queryset, many=True, fields=["id", "restaurants", "day", "items"]
        )
        return Response(serializer.data)


@method_decorator(csrf_exempt, name="dispatch")
class ItemViewSet(viewsets.ModelViewSet):
    """
    Item View Accept GET, POST
    return fields as per the ItemSerializer
    """

    http_method_names = ["get", "post"]
    authentication_classes = [TokenAuthentication]
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def update(self, request, pk=None):
        # returns forbidden when PUT request
        response = {"message": "Update function is not offered in this path."}
        return Response(response, status=status.HTTP_403_FORBIDDEN)

    def partial_update(self, request, pk=None):
        # returns forbidden when PATCH request
        response = {"message": "Update function is not offered in this path."}
        return Response(response, status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, pk=None):
        # returns forbidden when DELETE request
        response = {"message": "Delete function is not offered in this path."}
        return Response(response, status=status.HTTP_403_FORBIDDEN)


@method_decorator(csrf_exempt, name="dispatch")
class RatingViewSet(viewsets.ModelViewSet):
    """
    Rating View Accept GET, POST
    return fields as per the RatingSerializer
    """

    authentication_classes = [TokenAuthentication]
    queryset = Ratings.objects.all()
    serializer_class = RatingSerializer
    http_method_names = ["get", "post"]

    def create(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        today = datetime.today()
        user_rating = Ratings.objects.filter(
            menu=request.data.get("menu"),
            user=request.user,
            created_at__year=today.year,
            created_at__month=today.month,
            created_at__day=today.day,
        )
        if len(user_rating) >= 1:
            raise ValidationError({"rating": "user can rate only one menu."})
        serializer = RatingSerializer(data=request.data, context={"request": request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = ListRatingSerializer(queryset, many=True)
        return Response(serializer.data)

    def update(self, request, pk=None):
        # returns forbidden when PUT request
        response = {"message": "Update function is not offered in this path."}
        return Response(response, status=status.HTTP_403_FORBIDDEN)

    def partial_update(self, request, pk=None):
        # returns forbidden when PATCH request
        response = {"message": "Update function is not offered in this path."}
        return Response(response, status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, pk=None):
        # returns forbidden when DELETE request
        response = {"message": "Delete function is not offered in this path."}
        return Response(response, status=status.HTTP_403_FORBIDDEN)


@method_decorator(csrf_exempt, name="dispatch")
class ResultViewSet(viewsets.ModelViewSet):
    """
    Result View Accept GET, POST
    """

    authentication_classes = [TokenAuthentication]
    today = datetime.today()
    queryset = Ratings.objects.filter(
        created_at__year=today.year,
        created_at__month=today.month,
        created_at__day=today.day,
    )
    serializer_class = ListRatingSerializer
    http_method_names = ["get", "post"]
