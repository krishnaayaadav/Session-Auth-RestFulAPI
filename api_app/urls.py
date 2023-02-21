from django.urls import path
from .views import UserAPI

urlpatterns = [
    path('user-api/', UserAPI.as_view(), name='userapi'),
]
