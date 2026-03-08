from django.urls import path
from .views import instructor_courses

urlpatterns = [
    path('instructor/<int:instructor_id>/', instructor_courses, name="instructor_courses"),
]