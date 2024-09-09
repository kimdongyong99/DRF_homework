from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    def create(self, data):
        user = User.objects.create(
            username=["username"],
            password=["password"],
            email=data["email"],
            name=["name"],
            nickname=["nickname"],
            birthdate=["birthdate"],
            gender=data.get("gender", None),
            Self_introduction=data.get("Self_introduction", None),
        )
        return user

    class Meta:
        model = User
        fields = [
            "username",
            "password",
            "email",
            "name",
            "nickname",
            "birthdate",
            "gender",
            "Self_introduction",
        ]


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        exclude = "password"
