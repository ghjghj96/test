
from django.shortcuts import render
from django.urls import reverse
from students.models import Student
from django.http import HttpResponseRedirect

# Create your views here.

def regStudent(request):
    context= {'user_id':'aaa', 'user_pw':'1111'} #딕셔너리 형태로.
    return render(request, 'reg.html', context )


def regCon(request):
    name= request.POST.get('name')
    major= request.POST.get('major')
    age= request.POST.get('age')
    grade= request.POST.get('grade')
    gender= request.POST.get('gender')
    
    qs= Student(s_name= name, s_major= major, s_age= age, s_grade= grade, s_gender= gender)
    qs.save()
    return HttpResponseRedirect(reverse('students:reglist'))

def reglist(request):
    qs=Student.objects.all()
    context={'stuList':qs, 'count':qs.count()}
    return render(request, 'reglist.html', context)


#학생 상세페이지
def regview(request, name, major):
    #name= request.GET.get('name') 간단url은 애초에 호출되어 인자로 쓰는 거라서 이렇게 불러올 필요없음. 이건 파라미터 형식에서. 
    
    qs= Student.objects.get(s_name=name)
    context={'stu':qs}
    return render(request, 'regview.html', context)



#학생 상세페이지에서 학생 수정

def regmodify(request, name):
    qs = Student.objects.get(s_name=name)
    context={'stu':qs}
    return render(request, 'regmodify.html', context)


#학생 정보 수정 저장 후 학생리스트 페이지 이동
def regmodifyCon(request):
    name= request.POST.get('name')
    major= request.POST.get('major')
    age= request.POST.get('age')
    grade= request.POST.get('grade')
    gender= request.POST.get('gender')
    
    #db에서 찾아서 수정해야함. 생성이 아니라.
    qs= Student.objects.get(s_name=name)
    qs.s_major= major
    qs.s_age= age
    qs.s_grade= grade
    qs.s_gender = gender
    qs.save()
    return HttpResponseRedirect(reverse('students:reglist'))



def regdelete(request, name):
    qs = Student.objects.get(s_name=name)
    qs.delete()
    
    return HttpResponseRedirect(reverse('students:reglist'))