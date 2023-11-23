import random
from django.db import models
from django.utils.text import slugify

from users.models import User
from categories.models import Category

class Reading(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reading_value = models.DecimalField(max_digits=8, decimal_places=2)
    # 1. Glucose, 2. Carbs, 3. Medication Insulin, 4. Excersise, 5. Other Meds
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=False, blank=False, unique=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(f'{str(random.randint(1, 100))}{str(random.randint(1, 100))}{str(random.randint(1, 100))}{str(random.randint(1, 100))}{str(random.randint(1, 100))}{str(random.randint(1, 100))}-{str(self.category)}')
        super(Reading, self).save(*args, **kwargs)


    def __str__(self):
        return f"{self.reading_value} on {self.created_at}"
    

"""class Category(models.Model):
    name = models.CharField(max_length=50)
    units = models.CharField(max_length=20)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name"""