from django.urls import path
from profiles.api.views import (UserDetailAPIView, UserCreateListAPIView)

urlpatterns = [
    path('usuarios/', UserCreateListAPIView.as_view(), name='user-list'),
    path('usuarios/<int:pk>', UserDetailAPIView.as_view(), name='user-detail')
]
