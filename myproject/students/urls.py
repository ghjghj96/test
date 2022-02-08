
from . import views
from django.urls import include, path

app_name="students"
urlpatterns = [
  path('reg/', views.regStudent, name='reg'),
  path('regCon/', views.regStuCon, name='regCon'),
  path('regAll/', views.regStuAll, name='regAll'),
  path('search/', views.stuSearch, name='search'),
  path('nameSearch/', views.stuNameSearch, name='nameSearch')

]
