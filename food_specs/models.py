from django.db import models

# Create your models here.
#list = ['Alimento', 'Porción', 'Unidad', 'Peso Bruto (g)', 'Peso Neto (g)', 'Energia (Kcal)', 'Carbohidratos (g)', 'Clasificación']
class FoodInformation(models.Model):
    food = models.CharField(max_length=75)
    portion = models.CharField(max_length=10)
    units = models.CharField(max_length=10)
    gross_weight = models.CharField(max_length=6)
    net_weight = models.CharField(max_length=6)
    energy = models.CharField(max_length=6)
    carbs = models.CharField(max_length=6)
    clasification = models.CharField(max_length=75)


    def __str__(self):
        return self.food