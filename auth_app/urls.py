from django.urls import path
from .views import RegisterAPIView, LoginAPIView, LogoutAPIView, UserStatusAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='api_register'),
    path('login/', LoginAPIView.as_view(), name='api_login'),
    path('logout/', LogoutAPIView.as_view(), name='api_logout'),
    path('user/', UserStatusAPIView.as_view(), name='api_user_status'),
]