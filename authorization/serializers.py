from rest_framework import serializers
from .models import User

class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('__all__')


class UserViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('__all__')