from django.contrib import admin
from django.urls import path, include
from bite import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('tags/', views.cuisine_tags), # optional, parametru name='cuisine-tags-list-create' ca sa putem folosi numele URL-ului in loc sa-l tot scriem
    path('tags/<int:id>/', views.cuisine_tags_detail), # optional, parametru name='cuisine-tags-detail' ca sa putem folosi numele URL-ului in loc sa-l tot scriem

    # Auth endpoints
    path('api/auth/', include('dj_rest_auth.urls')),                # login/logout/password
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),  # signup

    # Social login via allauth
    path('api/auth/social/', include('allauth.socialaccount.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
