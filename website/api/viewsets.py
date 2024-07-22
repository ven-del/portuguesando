from rest_framework import viewsets
from website.api import serializers
from website import models

class StudentsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.StudentsSerializer
    queryset = models.Students.objects.all()