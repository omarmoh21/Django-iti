# students/models.py
from django.db import models
from courses.models import Course

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    courses = models.ManyToManyField(Course)
    photo = models.ImageField(upload_to='student_photos/', blank=True, null=True)

    def __str__(self):
        return self.name