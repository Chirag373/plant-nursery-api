from rest_framework import serializers
from api.models import Plant

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = "__all__"

    def validate_health(self, value):
        if not (0 <= int(value) <= 100):
            raise serializers.ValidationError("health must be between 0 to 100 range")
        return value