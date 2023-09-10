from rest_framework import serializers

from core.models import Declaration

class DeclarationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Declaration
        fields = (
            'fin_code',
            'password',
            'user_id',
            'dec_id',
        )


class ApplyDeclarationSerializer(serializers.Serializer):
    fin_code = serializers.CharField()
    password = serializers.CharField()
    dec_num = serializers.CharField()
