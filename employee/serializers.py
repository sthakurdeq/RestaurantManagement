from rest_framework import serializers
from .models import User
from datetime import date
import uuid

class UserSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(default=uuid.uuid4, editable=False)
    email = serializers.EmailField(unique=True)
    created_at = serializers.DateTimeField(auto_now_add=True)
    updated_at = serializers.DateTimeField(auto_now=True)

    class Meta:
        model = User
        fields = ('__all__')