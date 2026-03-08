from django.shortcuts import render, get_object_or_404
from .models import Student
from courses.models import Course

def course_students(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    students = Student.objects.filter(courses=course)

    return render(request, "students/student_list.html", {
        "course": course,
        "students": students
    })