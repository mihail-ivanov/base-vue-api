from django.urls import path

from . import views
from . import jwt_views


urlpatterns = [
    path('auth/obtain_token/', jwt_views.obtain_jwt_token_by_email),
    path('auth/refresh_token/', jwt_views.refresh_jwt_token),
]
