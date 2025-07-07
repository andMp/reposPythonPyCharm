from rest_framework import serializers
from .models import Zavd

class ZavdSerializer(serializers.ModelSerializer):
    class Meta:
        model=Zavd
        fields='__all__'