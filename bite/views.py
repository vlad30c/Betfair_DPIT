from django.http import JsonResponse
from .models import Tags
from .serializers import TagsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def cuisine_tags(request, format = None):
    """
    Get all cuisine tags (category='cuisine').
    Serialize them
    Return as JSON response.
    """
    if request.method == 'GET':
        queryset = Tags.objects.filter(category="cuisine")
        serializer = TagsSerializer(queryset, many=True)
        return Response({"cuisine types":serializer.data})

    if request.method == 'POST':
        serializer = TagsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(category="cuisine")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def cuisine_tags_detail(request, id, format=None):

    try:
        cuisine_tag = Tags.objects.get(pk=id, category="cuisine")
    except Tags.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TagsSerializer(cuisine_tag)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TagsSerializer(cuisine_tag, data=request.data)
        if serializer.is_valid():
            serializer.save(category="cuisine")
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        cuisine_tag.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)