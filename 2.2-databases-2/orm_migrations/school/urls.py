from django.urls import path

from school.views import students_list, add_teacher

urlpatterns = [
    path('', students_list, name='students'),
    path('add', add_teacher)
]
