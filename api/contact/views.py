from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.


class AuthView(APIView):
    def get(self, request, *args, **kwargs):
        q = request.query_params 
        email = q['email']
        password = q['password']
        try:
            username = User.objects.get(email=email)
        except ObjectDoesNotExist:
            raise Http404

        user = authenticate(username=username, password=password)
        if user is not None:
            serializer = UserSerializer(user)
            return Response(serializer.data)
        else:
            raise Http404

        #    snippets = Snippet.objects.all()
        #    serializer = SnippetSerializer(snippets, many=True)
        #    return Response(serializer.data)

        #def post(self, request, format=None):
        #    serializer = SnippetSerializer(data=request.DATA)
        #    if serializer.is_valid():
        #        serializer.save()
        #        return Response(serializer.data, status=status.HTTP_201_CREATED)
        #    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer




class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        username = data['username']
        email = data['email']
        password = data['password']
        try:
            user = User.objects.create_user(username, email, password)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except Exception, e:
            return Response(str(e))    


    #def list(self, request, *args, **kwargs):
    #    #print request.data
    #    print request.query_params
    #    return Response(request.query_params) 


    #def auth



