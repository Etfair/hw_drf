from django.shortcuts import render
from rest_framework import viewsets, generics

from users.models import User
from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer


class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
