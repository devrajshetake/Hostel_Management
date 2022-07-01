from django.urls import path
from . import views
from hostel import views as hostel_views

urlpatterns = [
    path('registration/',hostel_views.saveStudentDetails,name='registration'),
    path('',hostel_views.student_details,name='student_details'),
    path('add_student/',hostel_views.add_student,name='add_student'),


]