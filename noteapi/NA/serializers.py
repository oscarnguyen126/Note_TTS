from rest_framework import serializers
from .models import User, Note, Folder

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        field = ('__all__')

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        field = ('__all__')

class FolderSerializer(serializers.ModelSerializer):
    notes = NoteSerializer(many=True, read_only=True)
    class Meta:
        model = Folder
        field = ('__all__')