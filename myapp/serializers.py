from rest_framework import serializers
from .models import AiResponse

class ApiResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = AiResponse
        fields = '__all__'

        def validate_prompt(self, value):
            if not value.strip():
                raise serializers.ValidationError("Prompt cannot be empty.")
            return value

