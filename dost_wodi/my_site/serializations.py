from rest_framework import serializers
from .models import Zamovl

class ZamovlSerializer(serializers.ModelSerializer):
    class Meta:
        model=Zamovl
        fields='__all__'