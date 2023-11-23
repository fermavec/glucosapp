from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass


class Patient(User):
    class Meta:
        proxy = True

    
    def get_glucose(self):
        return []
    

class PatientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth = models.DateField()
    gender = models.BooleanField()
    bio = models.TextField()
    diabetic_since = models.DateField()
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    height = models.DecimalField(max_digits=10, decimal_places=2)