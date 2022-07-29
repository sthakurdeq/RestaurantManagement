from rest_framework import serializers
from .models import User
from datetime import date, datetime
import uuid

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password']