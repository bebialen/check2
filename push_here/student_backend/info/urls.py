from django.urls import path
from .views import create_student, get_all_students, get_single_student, update_delete_student

urlpatterns = [
    path('api/students/', create_student, name='create_student'),
    path('api/students/all/', get_all_students, name='get_all_students'),
    path('api/students/<int:pk>/', get_single_student, name='get_single_student'),
    path('api/students/<int:pk>/update_delete/', update_delete_student, name='update_delete_student'),
]
