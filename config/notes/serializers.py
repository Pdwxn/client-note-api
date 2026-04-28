from rest_framework import serializers
from .models import Note
from clients.models import Client

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'
        read_only_fields = ['user', 'created_at']
    
    def validate_title(self, value):
        if not value or value.strip() == '':
            return 'Untitled'
        return value

    def validate_client(self, value):
        user = self.context['request'].user

        if value.user != user:
            raise serializers.ValidationError("No tienes acceso a este cliente.")

        return value