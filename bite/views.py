from django.http import JsonResponse
from .models import Cuisinetypes
from .serializers import CuisineTypesSerializer

def cuisine_types(request):
    """
    Get all cuisine types.
    Serialize them
    Return as JSON response.
    """
    queryset = Cuisinetypes.objects.all()
    serializer = CuisineTypesSerializer(queryset, many=True)
    return JsonResponse({"cuisine types":serializer.data})
