from django.contrib import admin
from django.urls import path, include  # Add 'include' here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('savoylifebot.urls')),  # Include your app's URLs
]
