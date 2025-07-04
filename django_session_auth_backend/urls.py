from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), # Django Admin interface
    path('api/', include('auth_app.urls')), # Include API URLs from auth_app
]
