# courses/models.py
from django.db import models
from instructors.models import Instructor

class Course(models.Model):
    title = models.CharField(max_length=100)
    hours = models.IntegerField()
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to='course_thumbnails/', blank=True, null=True)

    def __str__(self):
        return self.title