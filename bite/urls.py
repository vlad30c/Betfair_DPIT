from django.contrib import admin
from django.urls import path, include
from bite import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('cuisine-types/', views.cuisine_types),
    path('cuisine-types/<int:id>/', views.cuisine_type_detail),

    # Auth endpoints
    path('api/auth/', include('dj_rest_auth.urls')),                # login/logout/password
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),  # signup

    # Social login via allauth
    path('api/auth/social/', include('allauth.socialaccount.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)