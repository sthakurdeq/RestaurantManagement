from rest_framework import serializers
from .models import User
from datetime import date, datetime
import uuid

class UserSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(default=uuid.uuid4)
    email = serializers.EmailField()
    created_at = serializers.DateTimeField(default=datetime.today)
    updated_at = serializers.DateTimeField(default=datetime.today)

    class Meta:
        model = User
        fields = ('__all__')