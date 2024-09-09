from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer, UserProfileSerializer
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404
from .models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, RetrieveAPIView


class UserCreate(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class Profile(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "username"
