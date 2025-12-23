from .models import WatchList
from rest_framework import serializers


class WatchListSerializer(serializers.ModelSerializer):
        class Meta:
                model = WatchList
                fields = ['id', 'user', 'crypto_symbol', 'target_price', 'created_at']
                read_only_fields = ['user']
        def validate_coin_symbol(self, value):
                if not value.isalnum():
                        raise serializers.ValidationError("Invalid cryptocurrency symbol.")
                return value.upper()
        