from rest_framework import serializers
from .models import BodyWeight

class BodyWeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = BodyWeight
        fields = ['user', 'weight', 'date']