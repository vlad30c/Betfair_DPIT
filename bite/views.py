from django.http import JsonResponse
from .models import Tags, Restaurants, RestaurantSchedules, RestaurantFiles, Ratings, Reservations, Favorites, Spotlight
from .serializers import TagsSerializer, RestaurantsSerializer, RestaurantSchedulesSerializer, RestaurantFilesSerializer, RatingsSerializer, ReservationsSerializer, FavoritesSerializer, SpotlightSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, permissions
from .serializers import UserUpdateSerializer
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from datetime import datetime
from django.db.models import Avg

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_spotlight(request):
    # Get query param ?city=Something
    city = request.query_params.get('city', None)

    # Base queryset
    spotlights = Spotlight.objects.all().order_by('-created_at')

    # If city provided, filter by restaurant's city
    if city:
        spotlights = spotlights.filter(restaurant__city__iexact=city)

    serializer = SpotlightSerializer(spotlights, many=True, context={'request': request})
    return Response({'spotlight': serializer.data}, status=status.HTTP_200_OK)

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
    Get all restaurants with optional filtering:
    - city (partial, case-insensitive)
    - search by restaurant name (partial)
    - multiple tags (AND filtering)
    - multiple price levels (OR filtering)
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
        
        # --- Filter by tag (cuisine/setting) ---
        tag_param = request.GET.get("tags")  # e.g. "Asian,Romantic"
        if tag_param:
            tags = [t.strip() for t in tag_param.split(",") if t.strip()]
            for t in tags:
                queryset = queryset.filter(tags__name__iexact=t)
        
        # --- Filter by price levels (OR filtering for multiple values) ---
        price_levels_param = request.GET.get("price_level", "")  # e.g. "budget-friendly,expensive"
        price_levels = [p.strip() for p in price_levels_param.split(",") if p.strip()]
        if price_levels:
            q = Q()
            for p in price_levels:
                q |= Q(price_level=p)
            queryset = queryset.filter(q)

        """
        # --- Filter by minimum rating ---
        min_rating = request.GET.get("min_rating")
        if min_rating:
            queryset = queryset.filter(avg_rating__gte=float(min_rating))
        """
        
        queryset = queryset.distinct()
        serializer = RestaurantsSerializer(queryset, many=True, context={'request': request})
        return Response({"restaurants": serializer.data})

    elif request.method == 'POST':
        serializer = RestaurantsSerializer(data=request.data, context={'request': request})
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


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def restaurant_file_detail(request, id, format=None):
    """
    GET: Get a single restaurant file.
    PUT/PATCH: Update a file (e.g., replace URL or type).
    DELETE: Remove a file.
    """
    try:
        file = RestaurantFiles.objects.get(pk=id)
    except RestaurantFiles.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RestaurantFilesSerializer(file)
        return Response(serializer.data)

    elif request.method in ['PUT', 'PATCH']:
        partial = request.method == 'PATCH'  # Allow partial updates
        serializer = RestaurantFilesSerializer(file, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        file.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ------------------ Cities ------------------

@api_view(['GET'])
def unique_cities(request):
    """
    Returns a list of unique cities from the Restaurants table.
    Optional query param 'search' filters cities containing the text.
    """
    search = request.GET.get('search', '')  # get the search param, default to empty string

    # Get all cities, optionally filter by search text
    cities = Restaurants.objects.exclude(city__isnull=True).exclude(city__exact='')
    if search:
        cities = cities.filter(city__icontains=search)
    
    # Extract city names and make unique
    unique_cities = sorted(set(cities.values_list('city', flat=True)))

    return Response({"cities": unique_cities})

# ------------------ Ratings ------------------

@api_view(['GET', 'POST'])
def ratings(request, format = None):
    if request.method == 'GET':
        restaurant_id = request.query_params.get('restaurant', None)
        limit = request.query_params.get('limit', None)

        queryset = Ratings.objects.all()
        if restaurant_id:
            queryset = queryset.filter(restaurant_id=restaurant_id)
        
        queryset = queryset.order_by('-rating_date')  # newest first
        
        if limit:
            queryset = queryset[:int(limit)]
            
        serializer = RatingsSerializer(queryset, many=True)
        return Response({"ratings": serializer.data})
    
    elif request.method == 'POST':
        # user will be automatically linked from the token
        serializer = RatingsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def restaurant_rating_summary(request, restaurant_id):
    ratings = Ratings.objects.filter(restaurant_id=restaurant_id)
    if not ratings.exists():
        return Response({"average": 0, "count": 0, "distribution": {i: 0 for i in range(1, 6)}})
    
    average = ratings.aggregate(Avg('score'))['score__avg']
    count = ratings.count()
    distribution = {i: ratings.filter(score=i).count() for i in range(1, 6)}
    
    return Response({
        "average": round(average, 1),
        "count": count,
        "distribution": distribution
    })

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
@permission_classes([IsAuthenticated])
def reservations(request):
    # GET → list all of the current user's reservations
    if request.method == 'GET':
        user_reservations = Reservations.objects.filter(user=request.user).order_by('-reservation_date', '-reservation_time')
        serializer = ReservationsSerializer(user_reservations, many=True)
        return Response({"reservations": serializer.data}, status=status.HTTP_200_OK)

    # POST → create a new reservation
    elif request.method == 'POST':
        serializer = ReservationsSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            reservation = serializer.save()
            return Response({
                "success": True,
                "message": "Reservation created successfully.",
                "reservation": ReservationsSerializer(reservation).data
            }, status=status.HTTP_201_CREATED)
        return Response({"success": False, "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    
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
