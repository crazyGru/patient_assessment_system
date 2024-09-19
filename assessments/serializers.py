from rest_framework import serializers
from .models import Patient, Assessment

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

    def validate_phone_number(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("Phone number must be numeric.")
        return value

class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = '__all__'

    def validate_final_score(self, value):
        if value < 0 or value > 100:
            raise serializers.ValidationError("Final score must be between 0 and 100.")
        return value