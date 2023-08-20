from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    invite_code = serializers.CharField(max_length=6, allow_null=True)
    class Meta:
        model = User
        fields = ('phone_number', 'auth_code', 'invite_code')