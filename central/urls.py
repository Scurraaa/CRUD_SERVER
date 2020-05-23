from django.urls import path
from central import views

urlpatterns = [
    path('student', views.add_retrieve_all_student),
    path('student/<int:student_number>', views.update_retrieve_delete_single_student),
]