from rest_framework import serializers
from .models import Tags, Menucategories, Menuitems, Menutypes, RestaurantSchedules, Ratings, Reservations, Restaurants, RestaurantFiles
from django.contrib.auth.models import User
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['phone_number', 'profile_picture']

class UserUpdateSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'profile']

    def update(self, instance, validated_data):
        # Extract profile data
        profile_data = validated_data.pop('profile', {})
        profile = instance.profile  

        # Update User fields
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        # Update Profile fields
        profile.phone_number = profile_data.get('phone_number', profile.phone_number)
        profile.profile_picture = profile_data.get('profile_picture', profile.profile_picture)
        profile.save()

        return instance


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


class RestaurantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurants
        fields = ['restaurant_id', 'name', 'description', 'email', 'phone_number','website',
                  'address', 'city', 'latitude', 'longitude', 'price_level', 'tags']


class RestaurantSchedulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantSchedules
        fields = ['schedule_id', 'restaurant', 'day_of_week', 'open_time', 'close_time']


class RestaurantFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantFiles
        fields = ['file_id', 'restaurant', 'file_url','type', 'uploaded_at_utc']
        read_only_fields = ['uploaded_at_utc']


class RatingsSerializer(serializers.ModelSerializer):
    user_display = serializers.SerializerMethodField() # read-only field, ca atunci cand user(adica cheia spre el)=0, sa poti afisa "Deleted user"

    class Meta:
        model = Ratings
        fields = ['rating_id', 'restaurant', 'user', 'user_display', 'score',
                  'comment', 'rating_date']

    def get_user_display(self, obj):
        if obj.user is None:
            return "Deleted user"
        return obj.user.username
    

class ReservationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservations
        fields = ['reservation_id', 'user', 'restaurant', 'reservation_date', 'reservation_time',
                  'number_of_guests', 'status', 'special_requests', 'booking_timestamp', 'phone_number']