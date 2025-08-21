from rest_framework import serializers
from .models import Cuisinetypes, Menucategories, Menuitems, Menutypes, Operatinghours, Ratings, Reservations, Restaurants, Users, Sysdiagrams

class CuisineTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuisinetypes
        fields = ['cuisine_type_id', 'cuisine_name']