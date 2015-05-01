from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
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

    def create(self, request, *args, **kwargs):
        print '***********'
        print args
        print kwargs
        data = request.data
        username = data['username']
        email = data['email']
        password = data['password']
        try:
            user = User.objects.create_user(username, email, password)
            return Response(str(user.id))
        except Exception, e:
            return Response(str(e))    
        
