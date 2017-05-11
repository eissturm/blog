from django.shortcuts import render
from rest_framework import viewsets, generics
from .serializers import UserSerializer
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, 'base.html', {})

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
