from rest_framework import serializers

from core.models import Declaration

class DeclarationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Declaration
        field = (
            'fin_code',
            'password',
            'user_id',
            'dec_id',
        )