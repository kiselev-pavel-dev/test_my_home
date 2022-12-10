from django.urls import path
from rest_framework.authtoken import views

from .views import EntityAPIView

app_name = "api"

urlpatterns = [
    path("entities/", EntityAPIView.as_view()),
    path('api-token-auth/', views.obtain_auth_token),
]
