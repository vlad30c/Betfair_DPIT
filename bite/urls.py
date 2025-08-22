from django.contrib import admin
from django.urls import path
from bite import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cuisine-types/', views.cuisine_types),
    path('cuisine-types/<int:id>/', views.cuisine_type_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)