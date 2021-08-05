from django.contrib.auth.models import User
from kanvas_app.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status


class AccountsView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        if User.objects.filter(username=serializer.validated_data['username']).exists():
            return Response({'error':'user already exist!'},status=status.HTTP_409_CONFLICT)

        user = User.objects.create_user(**serializer.validated_data)

        serializer = UserSerializer(user)

        return Response(serializer.data)

class LoginView(APIView):
    ...