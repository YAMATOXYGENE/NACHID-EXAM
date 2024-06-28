from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jokes/', include('jokes.urls')),  # Include the jokes app URLs
    path('accounts/', include('django.contrib.auth.urls')),  # For authentication
]
