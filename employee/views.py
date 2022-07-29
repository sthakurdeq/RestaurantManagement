from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .serializers import UserSerializer
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

class UserViewSet(viewsets.ViewSet):
    """
    A ViewSet for Users to create an employee
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def create(self, request):
        '''
        Create method to add an employee
        '''
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)