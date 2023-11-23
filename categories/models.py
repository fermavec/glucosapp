from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    units = models.CharField(max_length=20)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name