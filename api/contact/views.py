from django.shortcuts import render
from rest_framework import viewsets

from .models import *
from .serializers import *
from django.contrib.auth.models import User
# Create your views here.


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


