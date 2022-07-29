# Create your views here.
from .models import User
from .serializers import UserSerializer
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


@method_decorator(csrf_exempt, name="dispatch")
class UserViewSet(viewsets.ModelViewSet):
    """
    Create a Users Accepts POST,GET
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def update(self, request, pk=None):
        response = {"message": "Update function is not offered in this path."}
        return Response(response, status=status.HTTP_403_FORBIDDEN)

    def partial_update(self, request, pk=None):
        response = {"message": "Update function is not offered in this path."}
        return Response(response, status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, pk=None):
        response = {"message": "Delete function is not offered in this path."}
        return Response(response, status=status.HTTP_403_FORBIDDEN)
