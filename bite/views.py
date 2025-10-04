from django.http import JsonResponse
from .models import Tags, Restaurants, RestaurantSchedules, RestaurantFiles, Ratings, Reservations, Favorites
from .serializers import TagsSerializer, RestaurantsSerializer, RestaurantSchedulesSerializer, RestaurantFilesSerializer, RatingsSerializer, ReservationsSerializer, FavoritesSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, permissions
from .serializers import UserUpdateSerializer
from rest_framework.permissions import IsAuthenticated

class UpdateAuthenticatedUserView(generics.UpdateAPIView):
    serializer_class = UserUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_current_user(request):
    if not request.user or not request.user.is_authenticated:
        return Response(
            {"detail": "Invalid or missing token."},
            status=status.HTTP_401_UNAUTHORIZED
        )
    
    serializer = UserUpdateSerializer(request.user)
    return Response(serializer.data)


# ------------------ Tags ------------------

ALLOWED_TAG_CATEGORIES = [choice[0] for choice in Tags.CATEGORY_CHOICES]


@api_view(['GET'])
def tag_categories(request):
    """
    Return the allowed tag categories.
    tags/
    """
    categories = {key: label for key, label in Tags.CATEGORY_CHOICES}
    return Response({"tag_categories": categories})


@api_view(['GET', 'POST'])
def tags_by_category(request, category, format=None):
    """
    tags/<str:category>/
    """
    if category not in ALLOWED_TAG_CATEGORIES:
        return Response({"error": f"Invalid category '{category}'. Allowed: {ALLOWED_TAG_CATEGORIES}"}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        queryset = Tags.objects.filter(category=category)
        serializer = TagsSerializer(queryset, many=True)
        return Response({f"{category}_tags": serializer.data})

    elif request.method == 'POST':
        serializer = TagsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(category=category)  # force the category
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def tag_detail_by_category(request, category, id, format=None):
    """
    tags/<str:category>/<int:id>/
    """
    if category not in ALLOWED_TAG_CATEGORIES:
        return Response({"error": f"Invalid category '{category}'. Allowed: {ALLOWED_TAG_CATEGORIES}"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        tag = Tags.objects.get(pk=id, category=category)
    except Tags.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TagsSerializer(tag)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TagsSerializer(tag, data=request.data)
        if serializer.is_valid():
            serializer.save(category=category)  # force category
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        tag.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  


# ------------------ Restaurants ------------------

@api_view(['GET', 'POST'])
def restaurants(request, format=None):
    """
    Get all restaurant tags.
    Serialize them
    Return as JSON/HTTP response.
    """
    if request.method == 'GET':
        queryset = Restaurants.objects.all()
        
        # --- Filtering by city (partial match, case-insensitive) ---
        city = request.GET.get("city", "")
        if city:
            queryset = queryset.filter(city__icontains=city)

        # --- Searching by partial restaurant name ---
        search = request.GET.get("search")
        if search:
            queryset = queryset.filter(name__icontains=search)
        
        # --- Filter by price level ---
        price_level = request.GET.get("price_level")
        if price_level:
            queryset = queryset.filter(price_level=price_level)

         # --- Filter by tag (cuisine/setting) ---
        tag_param = request.GET.get("tags")  # e.g. "Asian,Romantic"
        if tag_param:
            tags = [t.strip() for t in tag_param.split(",") if t.strip()]
            for t in tags:
                queryset = queryset.filter(tags__name__iexact=t)
        """
        # --- Filter by minimum rating ---
        min_rating = request.GET.get("min_rating")
        if min_rating:
            queryset = queryset.filter(avg_rating__gte=float(min_rating))
        """
        
        queryset = queryset.distinct()
        serializer = RestaurantsSerializer(queryset, many=True)
        return Response({"restaurants": serializer.data})

    elif request.method == 'POST':
        serializer = RestaurantsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def restaurant_detail(request, id, format=None):
    try:
        restaurant = Restaurants.objects.get(pk=id)
    except Restaurants.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        serializer = RestaurantsSerializer(restaurant)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RestaurantsSerializer(restaurant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        restaurant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# ------------------ RestaurantSchedules ------------------

@api_view(['GET', 'POST'])
def restaurant_schedules(request, format=None):
    if request.method == 'GET':
        queryset = RestaurantSchedules.objects.all()
        serializer = RestaurantSchedulesSerializer(queryset, many=True)
        return Response({"restaurant_schedules": serializer.data})

    elif request.method == 'POST':
        serializer = RestaurantSchedulesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def restaurant_schedule_detail(request, id, format=None):
    try:
        schedule = RestaurantSchedules.objects.get(pk=id)
    except RestaurantSchedules.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        serializer = RestaurantSchedulesSerializer(schedule)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RestaurantSchedulesSerializer(schedule, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        schedule.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ------------------ RestaurantFiles ------------------

@api_view(['GET', 'POST'])
def restaurant_files(request, format=None):
    """
    GET: Return all restaurant files (with optional filtering).
    POST: Upload a new restaurant file (menu, photo, etc).
    """
    if request.method == 'GET':
        queryset = RestaurantFiles.objects.all()

        # --- Optional filters ---
        restaurant_id = request.GET.get("restaurant_id")
        if restaurant_id:
            queryset = queryset.filter(restaurant__restaurant_id=restaurant_id)

        file_type = request.GET.get("type")
        if file_type:
            queryset = queryset.filter(type__iexact=file_type)

        serializer = RestaurantFilesSerializer(queryset, many=True)
        return Response({"restaurant_files": serializer.data})
    
    elif request.method == 'POST':
        serializer = RestaurantFilesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def restaurant_file_detail(request, id, format=None):
    """
    GET: Get a single restaurant file.
    DELETE: Remove a file.
    """
    try:
        file = RestaurantFiles.objects.get(pk=id)
    except RestaurantFiles.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RestaurantFilesSerializer(file)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        file.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ------------------ Ratings ------------------

@api_view(['GET', 'POST'])
def ratings(request, format = None):
    if request.method == 'GET':
        queryset = Ratings.objects.all()
        serializer = RatingsSerializer(queryset, many=True)
        return Response({"ratings":serializer.data})

    elif request.method == 'POST':
        serializer = RatingsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def rating_detail(request, id, format=None):

    try:
        rating = Ratings.objects.get(pk=id)
    except Ratings.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        serializer = RatingsSerializer(rating)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = RatingsSerializer(rating, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        rating.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# ------------------ Reservations ------------------

@api_view(['GET', 'POST'])
def reservations(request, format=None):
    if request.method == 'GET':
        queryset = Reservations.objects.all()
        serializer = ReservationsSerializer(queryset, many=True)
        return Response({"reservations": serializer.data})

    elif request.method == 'POST':
        serializer = ReservationsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def reservation_detail(request, id, format=None):
    try:
        reservation = Reservations.objects.get(pk=id)
    except Reservations.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ReservationsSerializer(reservation)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ReservationsSerializer(reservation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        reservation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# ------------------ Favorites ------------------

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def favorites_list(request):
    """
    Get all favorite restaurants of the authenticated user.
    """
    favorites = Favorites.objects.filter(user=request.user)
    serializer = FavoritesSerializer(favorites, many=True)
    return Response({"favorites": serializer.data}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def toggle_favorite(request):
    """
    Toggle a restaurant as favorite.
    If already favorited → remove it.
    If not favorited → add it.
    """
    restaurant_id = request.data.get('restaurant')
    if not restaurant_id:
        return Response({"error": "Restaurant ID required"}, status=status.HTTP_400_BAD_REQUEST)

    restaurant = Restaurants.objects.filter(restaurant_id=restaurant_id).first()
    if not restaurant:
        return Response({"error": "Restaurant not found"}, status=status.HTTP_404_NOT_FOUND)

    favorite = Favorites.objects.filter(user=request.user, restaurant=restaurant).first()

    if favorite:
        # Already favorited → remove it
        favorite.delete()
        return Response({"message": "Removed from favorites", "favorited": False}, status=status.HTTP_200_OK)
    else:
        # Not favorited → add it
        favorite = Favorites.objects.create(user=request.user, restaurant=restaurant)
        return Response({"message": "Added to favorites", "favorited": True}, status=status.HTTP_201_CREATED)
