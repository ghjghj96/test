"""stuPjt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

app_name = 'students'
urlpatterns = [
    path('reg/', views.regStudent, name='reg'),
    path('reglist/', views.reglist, name='reglist'),
    path('<str:name>/<str:major>/regview/', views.regview, name='regview'),
    path('<str:name>/regmodify/', views.regmodify, name='regmodify'),
    path('regCon/', views.regCon, name='regCon'),
    path('regmodifyCon/', views.regmodifyCon, name='regmodifyCon'),
    path('<str:name>/regdelete/', views.regdelete, name='regdelete'),
]
