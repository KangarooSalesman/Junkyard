from rest_framework import generics
from .serializers import UserSerializer
from django.contrib.auth import get_user_model


class RegisterView(generics.CreateAPIView):
    User = get_user_model()
    queryset = User.objects.all()

    serializer_class = UserSerializer
