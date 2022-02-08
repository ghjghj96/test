from django.shortcuts import render

# Create your views here.

def index(request):
    #뷰에서 html로 보낼때는 딕셔너리로.
    #html에서 뷰로 보낼때는 form, parameter, 간편url
    context={"user_id":'admin', 'u_count':100}
    return render(request, 'index.html', context)