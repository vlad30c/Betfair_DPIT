from django.contrib import admin
from django.urls import path
from bite import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cuisine-types/', views.cuisine_types),
]