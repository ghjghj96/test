from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from students.models import Student

# Create your views here.
def regStudent(request):
    context = {'user_id':'aaaa', 'user_pw':'1111'}
    return render(request, 'reg.html', context)

def regCon(request):
    name = request.POST.get('name')
    major = request.POST.get('major')
    age = request.POST.get('age')
    grade = request.POST.get('grade')
    gender = request.POST.get('gender')
    print(name)
    qs = Student(s_name = name, s_major = major, s_age = age, s_grade = grade, s_gender = gender)
    qs.save()
    return HttpResponseRedirect(reverse('students:reglist'))

def reglist(request):
    qs = Student.objects.all()
    s_count = qs.count()
    context = {'stuList': qs, 'count': s_count}
    return render(request, 'reglist.html', context)

#학생 상세페이지
def regview(request, name, major):
    # name = request.GET.get('name') 파라미터 방식
    print('views :', name)
    print('views :', major)
    qs = Student.objects.get(s_name=name)
    context = {'stu':qs}
    return render(request, 'regview.html', context)

# 학생정보수정페이지
def regmodify(request, name):
    qs = Student.objects.get(s_name=name)
    context = {'stu':qs}
    return render(request, 'regmodify.html', context)

# 학생정보수정 저장 후 학생리스트 페이지 이동
def regmodifyCon(request):
    name = request.POST.get('name')
    major = request.POST.get('major')
    age = request.POST.get('age')
    grade = request.POST.get('grade')
    gender = request.POST.get('gender')
    
    # db에 정보 찾기
    qs = Student.objects.get(s_name = name)
    qs.s_major = major
    qs.s_age = age 
    qs.s_grade = grade
    qs.s_gender = gender
    qs.save()
    
    return HttpResponseRedirect(reverse('students:reglist'))

# 학생정보 삭제
def regdelete(request, name):
    qs = Student.objects.get(s_name = name)
    qs.delete()
    
    return HttpResponseRedirect(reverse('students:reglist'))