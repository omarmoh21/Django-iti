from django.shortcuts import render
from .models import Instructor

def instructor_list(request):
    instructors = Instructor.objects.all()
    return render(request, "instructors/instructor_list.html", {"instructors": instructors})