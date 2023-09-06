
from django.db.models import QuerySet

from rest_framework import generics, permissions
from rest_framework.response import Response


from .serializers import DeclarationSerializer


class DeclarationListApiView(generics.ListAPIView):
    serializer_class = DeclarationSerializer
    permission_classes = (permissions.IsAuthenticated,)


class DeclarationCreateApiView(generics.CreateAPIView):
    serializer_class = DeclarationSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()
        serializer.save(user_id=request.user.id)
        return Response(serializer.data)