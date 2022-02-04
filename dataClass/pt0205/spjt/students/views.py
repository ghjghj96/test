from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from students.models import Student

# Create your views here.
def regStudent(request):
    return render(request, 'reg.html')


def regStuCon(request):
    name = request.POST["name"]
    major = request.POST["major"]
    age = request.POST["age"]
    grade = request.POST["grade"]
    gender = request.POST["gender"]
    
    qs = Student(s_name = name, s_major = major, s_age = age, s_grade = grade, s_gender = gender)
    qs.save()
    return HttpResponseRedirect(reverse('index'))

def regStuAll(request):
    qs = Student.objects.all()
    context = {'stuList':qs}
    return render(request,'stuList.html', context)