from django.urls import path
from .views import instructor_list

urlpatterns = [
    path('', instructor_list, name="instructor_list"),
]