from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework import viewsets, status
from rest_framework.response import Response

from restaurant.models import Restaurant, Item, Menu
from restaurant.serializers import RestaurantSerializer, MenuSerializer, ItemSerializer


@method_decorator(csrf_exempt, name='dispatch')
class RestuarantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    
    def update(self, request, pk=None):
        response = {'message': 'Update function is not offered in this path.'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)

    def partial_update(self, request, pk=None):
        response = {'message': 'Update function is not offered in this path.'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)

    # def destroy(self, request, pk=None):
    #     response = {'message': 'Delete function is not offered in this path.'}
    #     return Response(response, status=status.HTTP_403_FORBIDDEN)

@method_decorator(csrf_exempt, name='dispatch')
class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
    # def update(self, request, pk=None):
    #     response = {'message': 'Update function is not offered in this path.'}
    #     return Response(response, status=status.HTTP_403_FORBIDDEN)

    # def partial_update(self, request, pk=None):
    #     response = {'message': 'Update function is not offered in this path.'}
    #     return Response(response, status=status.HTTP_403_FORBIDDEN)

    # def destroy(self, request, pk=None):
    #     response = {'message': 'Delete function is not offered in this path.'}
    #     return Response(response, status=status.HTTP_403_FORBIDDEN)

@method_decorator(csrf_exempt, name='dispatch')
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    
    def update(self, request, pk=None):
        response = {'message': 'Update function is not offered in this path.'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)

    def partial_update(self, request, pk=None):
        response = {'message': 'Update function is not offered in this path.'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, pk=None):
        response = {'message': 'Delete function is not offered in this path.'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)