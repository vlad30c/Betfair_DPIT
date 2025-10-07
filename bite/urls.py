from django.contrib import admin
from django.urls import path, include
from bite import views
from rest_framework.urlpatterns import format_suffix_patterns
from .views import UpdateAuthenticatedUserView, get_current_user, toggle_favorite, favorites_list


urlpatterns = [
    # Tags endpoints
    path('tags/', views.tag_categories), # GET only endpoint for getting the list of tags
    path('tags/<str:category>/', views.tags_by_category), # optional, parametru name='tags_by_category' ca sa putem folosi numele URL-ului in loc sa-l tot scriem
    path('tags/<str:category>/<int:id>/', views.tag_detail_by_category), # optional, parametru name='tag_detail_by_category' ca sa putem folosi numele URL-ului in loc sa-l tot scriem

    # Restaurant endpoints
    path('restaurants/', views.restaurants),
    path('restaurants/<int:id>/', views.restaurant_detail),

    # Restaurant files endpoint
    path('restaurantfiles/', views.restaurant_files),
    path('restaurantfiles/<int:id>/', views.restaurant_file_detail),

    # Unique cities ednpoint
    path('restaurants/cities/', views.unique_cities, name='unique_cities'),
    
    # Auth endpoints
    path('api/auth/', include('dj_rest_auth.urls')),                # login/logout/password
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),  # signup
    path('api/me/update/', UpdateAuthenticatedUserView.as_view(), name='update-user'),
    path('api/users/me/', get_current_user, name='get-current-user'),

    # Reservation endpoint
    path('reservations/', views.reservations, name='reservations'),

    # Favorites endpoints
    path('favorites/toggle/', toggle_favorite, name='favorites-toggle'),
    path('favorites/', favorites_list, name='favorites-list'),

    # Ratings endpoints
    path('ratings/', views.ratings),
    path('ratings/<int:id>/', views.rating_detail),
    path('ratings/<int:restaurant_id>/', views.restaurant_rating_summary),
]

urlpatterns = format_suffix_patterns(urlpatterns)
