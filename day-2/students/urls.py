from django.urls import path
from .views import course_students

urlpatterns = [
    path('course/<int:course_id>/', course_students, name="course_students"),
]