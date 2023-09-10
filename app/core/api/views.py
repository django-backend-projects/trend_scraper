from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from ..tasks import run_apply_declarations

from .serializers import ApplyDeclarationSerializer


class ApplySmartCustomsView(generics.GenericAPIView):
    serializer_class = ApplyDeclarationSerializer
    permission_classes = (AllowAny,)

    def post(self, *args, **kwargs):
        serializer = self.serializer_class(
            data=self.request.data.get("declarations", "[]"),
            many=True,
        )
        serializer.is_valid(raise_exception=True)

        for declaration in serializer.validated_data:
            run_apply_declarations.apply_async(args=[
                declaration.get('dec_num'),
                declaration.get('fin_code'),
                declaration.get('password')
            ])

        return Response({"message": "OK"}, status=200)
