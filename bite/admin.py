from django.contrib import admin
from .models import Cuisinetypes, Menucategories, Menuitems, Menutypes, Operatinghours, Ratings, Reservations, Restaurants, Users, Sysdiagrams
# Register your models here.


admin.site.register(Cuisinetypes)
admin.site.register(Menucategories)
admin.site.register(Menuitems)
admin.site.register(Menutypes)
admin.site.register(Operatinghours)
admin.site.register(Ratings)
admin.site.register(Reservations)
admin.site.register(Restaurants)
admin.site.register(Users)
admin.site.register(Sysdiagrams)