from django.contrib import admin
from .models import Tags, Menucategories, Menuitems, Menutypes, RestaurantSchedules, Ratings, Reservations, Restaurants, Users, RestaurantFiles
# Register your models here.


admin.site.register(Tags)
admin.site.register(Restaurants)
admin.site.register(RestaurantSchedules)
admin.site.register(RestaurantFiles)
admin.site.register(Menutypes)
admin.site.register(Menucategories)
admin.site.register(Menuitems)
admin.site.register(Ratings)
admin.site.register(Reservations)
admin.site.register(Users)
