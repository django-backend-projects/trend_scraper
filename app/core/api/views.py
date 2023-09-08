
from django.db.models import QuerySet

from rest_framework import generics, permissions
from rest_framework.response import Response

from core.models import Declaration


from .serializers import DeclarationSerializer


class DeclarationListApiView(generics.ListAPIView):
    serializer_class = DeclarationSerializer
    queryset = Declaration.objects.filter(is_declared=False)


class DeclarationCreateApiView(generics.CreateAPIView):
    queryset = Declaration.objects.all()
    serializer_class = DeclarationSerializer
