from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'user_id':'홍길동', 'nickname':'길동스'}
    return render(request, 'index.html', context)