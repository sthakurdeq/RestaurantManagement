from datetime import datetime

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication

from restaurant.models import Ratings, Restaurant, Item, Menu
from restaurant.serializers import (
    RatingSerializer,
    RestaurantSerializer,
    MenuSerializer,
    ItemSerializer,
)


@method_decorator(csrf_exempt, name="dispatch")
class RestuarantViewSet(viewsets.ModelViewSet):
    '''
    Restaurant View Accept GET, POST, DELETE
    return fields as per the RestaurantSerializer
    '''
    queryset = Restaurant.objects.all()
    # authentication_classes = [TokenAuthentication]
    serializer_class = RestaurantSerializer

    def update(self, request, pk=None):
        # returns forbidden when PUT request
        response = {'message': 'Update function is not offered in this path.'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)

    def partial_update(self, request, pk=None):
        # returns forbidden when PATCH request
        response = {'message': 'Update function is not offered in this path.'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)

@method_decorator(csrf_exempt, name='dispatch')
class MenuViewSet(viewsets.ModelViewSet):
    '''
    Menu View Accept GET, POST, PUT, PATCH, DELETE
    return fields as per the MenuSerializer
    '''
    queryset = Menu.objects.all()
    authentication_classes = [TokenAuthentication]
    serializer_class = MenuSerializer

    def create(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        data = request.data
        serializer = MenuSerializer(
            data=data, fields=["id", "restaurants", "day", "item"]
        )
        if serializer.is_valid(raise_exception=True):
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
    '''
    Menu View Accept GET
    return todays menu based on date and day
    '''
    authentication_classes = [TokenAuthentication]
    today = datetime.today()
    day = {
        1: "MON",
        2: "TUE",
        3: "WED",
        4: "THUR",
        5: "FRI",
    }
    weekday = datetime.now().weekday()
    queryset = Menu.objects.filter(
        created_at__year=today.year,
        created_at__month=today.month,
        created_at__day=today.day,
        day=day.get(weekday),
    )
    serializer_class = MenuSerializer


@method_decorator(csrf_exempt, name="dispatch")
class ItemViewSet(viewsets.ModelViewSet):
    '''
    Item View Accept GET, POST
    return fields as per the ItemSerializer
    '''
    authentication_classes = [TokenAuthentication]
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def update(self, request, pk=None):
        # returns forbidden when PUT request
        response = {'message': 'Update function is not offered in this path.'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)

    def partial_update(self, request, pk=None):
        # returns forbidden when PATCH request
        response = {'message': 'Update function is not offered in this path.'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, pk=None):
        # returns forbidden when DELETE request
        response = {'message': 'Delete function is not offered in this path.'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)


@method_decorator(csrf_exempt, name="dispatch")
class RatingViewSet(viewsets.ModelViewSet):
    '''
    Rating View Accept GET, POST
    return fields as per the RatingSerializer
    '''
    queryset = Ratings.objects.all()
    serializer_class = RatingSerializer

    def update(self, request, pk=None):
        # returns forbidden when PUT request
        response = {'message': 'Update function is not offered in this path.'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)

    def partial_update(self, request, pk=None):
        # returns forbidden when PATCH request
        response = {'message': 'Update function is not offered in this path.'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, pk=None):
        # returns forbidden when DELETE request
        response = {'message': 'Delete function is not offered in this path.'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)
