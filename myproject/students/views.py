from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from students.models import Student

# Create your views here.

def regStudent(request):
    return render(request, 'reg.html')

def regStuCon(request):
    name = request.POST.get('name')
    major = request.POST.get('major')
    age = request.POST.get('age')
    grade = request.POST.get('grade')
    gender = request.POST.get('gender')

    qs= Student(s_name= name, s_major= major, s_age= age, s_grade= grade, s_gender= gender)
    qs.save()

    return HttpResponseRedirect(reverse('index'))

def regStuAll(request):
    qs = Student.objects.all()
    qscount = qs.count()
    context = {'stuList':qs, 'stuCount':qscount}
    return render(request, 'stuList.html', context)


def stuSearch(request):
    return render(request, 'search.html')


def stuNameSearch(request):
    name = request.POST.get('nameSearch')
    qs = Student.objects.filter(s_name__contains=name)
    context = {'outcomes':qs}
    return render(request, 'search.html', context)




    

    