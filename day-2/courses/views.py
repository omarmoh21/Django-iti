from django.shortcuts import render, get_object_or_404
from .models import Course
from instructors.models import Instructor

def instructor_courses(request, instructor_id):
    instructor = get_object_or_404(Instructor, id=instructor_id)
    courses = Course.objects.filter(instructor=instructor)

    return render(request, "courses/course_list.html", {
        "instructor": instructor,
        "courses": courses
    })