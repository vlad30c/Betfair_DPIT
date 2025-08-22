from django.http import JsonResponse
from .models import Cuisinetypes
from .serializers import CuisineTypesSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def cuisine_types(request, format = None):
    """
    Get all cuisine types.
    Serialize them
    Return as JSON response.
    """
    if request.method == 'GET':
        queryset = Cuisinetypes.objects.all()
        serializer = CuisineTypesSerializer(queryset, many=True)
        return Response({"cuisine types":serializer.data})

    if request.method == 'POST':
        serializer = CuisineTypesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def cuisine_type_detail(request, id, format=None):

    try:
        cuisine_type = Cuisinetypes.objects.get(pk=id)
    except Cuisinetypes.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CuisineTypesSerializer(cuisine_type)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CuisineTypesSerializer(cuisine_type, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        cuisine_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)