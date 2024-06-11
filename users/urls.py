from django.urls import path
from .views import UserByGender

urlpatterns = [
    path('<str:gender>/', UserByGender.as_view()),
]