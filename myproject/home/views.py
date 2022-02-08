from django.shortcuts import render

# Create your views here.

def index(request):
    context = {'user_id':'naraek', 'nickName':'나래😎'}
    return render(request, 'index.html', context)