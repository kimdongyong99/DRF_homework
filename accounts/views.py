from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import SignUpSerializer, LoginSerializer, ProFileSerializer
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404
from .models import User
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class SignUpAPIView(APIView):

    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)


class LoginAPIView(APIView):

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


class ProfileDetail(APIView):

    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        serializer = ProFileSerializer(user)
        return Response(serializer.data)
