from django.db import models
from uuid import uuid4

class Students(models.Model):
    id_student = models.UUIDField(primary_key=uuid4, editable=False)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    GENDERS = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    gender = models.CharField(max_length=1, choices=GENDERS)


