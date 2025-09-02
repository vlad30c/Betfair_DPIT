from rest_framework import serializers
from .models import Cuisinetypes, Menucategories, Menuitems, Menutypes, Operatinghours, Ratings, Reservations, Restaurants, Sysdiagrams, Users
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth.models import User

from rest_framework import serializers
from django.contrib.auth.models import User

from rest_framework import serializers
from django.contrib.auth.models import User

from rest_framework import serializers
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def validate(self, attrs):
        # Passwords must match
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Passwords must match."})
        # Username must be unique
        if User.objects.filter(username=attrs['username']).exists():
            raise serializers.ValidationError({"username": "Username is already in use."})
        # Email must be unique
        if User.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError({"email": "Email is already in use."})
        return attrs

    def save(self, **kwargs):
        validated_data = self.validated_data
        validated_data.pop('password2')
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password1']
        )
        return user


class CuisineTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuisinetypes
        fields = ['cuisine_type_id', 'cuisine_name']