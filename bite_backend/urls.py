
from django.http import HttpResponse
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Bite app endpoints
    path('', include('bite.urls')),
    path('test/', lambda request: HttpResponse('It works!')),
]
