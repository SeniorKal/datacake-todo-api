from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from .serializers import RegisterSerializer
# Create your views here.

User = get_user_model()

@api_view(["GET"])
def health_check(request):
    return Response({"status": "ok"})

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]