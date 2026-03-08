# instructors/models.py
from django.db import models

class Instructor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    department = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='instructors_photos/', blank=True, null=True)

    def __str__(self):
        return self.name