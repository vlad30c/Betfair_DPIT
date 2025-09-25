from django.http import JsonResponse
from .models import Tags, Restaurants, RestaurantSchedules, RestaurantFiles, Ratings, Reservations
from .serializers import TagsSerializer, RestaurantsSerializer, RestaurantSchedulesSerializer, RestaurantFilesSerializer, RatingsSerializer, ReservationsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

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
    if request.method == 'GET':
        queryset = RestaurantFiles.objects.all()
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