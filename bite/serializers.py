from rest_framework import serializers
from .models import Tags, Menucategories, Menuitems, Menutypes, RestaurantSchedules, Ratings, Reservations, Restaurants, Users, RestaurantFiles
from django.contrib.auth.models import User
from dj_rest_auth.registration.serializers import RegisterSerializer

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


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ['tag_id', 'name', 'category']
        read_only_fields = ['category']  # optional, prevents changing category via API

    def create(self, validated_data):
        # Optionally enforce category if you want to force cuisine tags
        category = validated_data.get('category')
        if category not in ['cuisine', 'setting']:
            raise serializers.ValidationError("Invalid category for tag.")
        return super().create(validated_data)