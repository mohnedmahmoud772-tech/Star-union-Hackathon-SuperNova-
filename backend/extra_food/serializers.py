from rest_framework import serializers

from .models import ExtraFood


class ProviderNestedSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    establishment_name = serializers.CharField()
    address = serializers.CharField()


class ExtraFoodSerializer(serializers.ModelSerializer):
    provider = ProviderNestedSerializer(read_only=True)

    class Meta:
        model = ExtraFood
        fields = [
            'id',
            'provider',
            'description',
            'category',
            'price',
            'quantity',
            'quantity_unit',
            'shelf_life',
            'status',
        ]
