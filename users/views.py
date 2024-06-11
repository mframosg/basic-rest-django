from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class UserByGender(APIView):
    def get(self, request, gender):
        names = {
            "men": ["Juan", "Pedro", "Pablo", "Jose"],
            "women": ["Maria"]
        }
        return Response({gender: names.get(gender, [])})