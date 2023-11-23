import random
from django.db import models
from django.utils.text import slugify

from users.models import User

class Anxiety(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    anxiety_level = models.IntegerField()
    panic_attack = models.BooleanField()
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=False, blank=False, unique=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(f'{str(random.randint(1, 100))}{str(random.randint(1, 100))}{str(random.randint(1, 100))}{str(random.randint(1, 100))}{str(random.randint(1, 100))}{str(random.randint(1, 100))}')
        super(Anxiety, self).save(*args, **kwargs)


    def __str__(self):
        return f"{self.user} anxiety on {self.created_at}"