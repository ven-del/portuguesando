from rest_framework import serializers
from website import models

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Students
        fields = '__all__'
