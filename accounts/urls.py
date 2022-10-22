from .views import RegisterView, UserDetailsView, UpdateProfileView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from django.urls import path


urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token'),
    path('login/refresh/', TokenRefreshView.as_view(), name='refresh_token'),
    path('register/', RegisterView.as_view()),
    path('fetch_user/', UserDetailsView.as_view()),
    path('update_profile/', UpdateProfileView.as_view()),
]
