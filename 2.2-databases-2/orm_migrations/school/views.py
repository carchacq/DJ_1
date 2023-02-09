from django.views.generic import ListView
from django.http import HttpResponse
from django.shortcuts import render
import random
from .models import Student, Teacher


def students_list(request):
    template = 'school/students_list.html'
    students = Student.objects.all().prefetch_related('teachers').order_by('group')
    context = {'object_list': students}
    return render(request, template, context)

def add_teacher(request):
    students = Student.objects.all()
    teachers = Teacher.objects.all()
    for student in students:
        random = teachers.order_by('?').first()
        student.teachers.add(random)
    return HttpResponse('Учителя назначены')

