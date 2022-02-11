from rest_framework import serializers
from .models import ExerciseActivity

class ExerciseActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseActivity
        fields = ['user', 'exercise', 'weight_amount', 'weight_date']