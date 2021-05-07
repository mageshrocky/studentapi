from django.urls import path
from .views import create_student, update_student_details, add_mark, update_mark

urlpatterns=[
    path('', create_student),
    path('<int:rn>/', update_student_details),
    path('add_mark/', add_mark),
    path('add_mark/<int:id>/', update_mark),
]