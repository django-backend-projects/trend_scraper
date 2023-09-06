
from django.db.models import QuerySet

from rest_framework import generics, permissions
from rest_framework.response import Response


from .serializers import DeclarationSerializer


class DeclarationListApiView(generics.ListAPIView):
    serializer_class = DeclarationSerializer
    permission_classes = (permissions.IsAuthenticated,)
