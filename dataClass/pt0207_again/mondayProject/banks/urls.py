
from django.urls import path, include
from . import views

app_name='banks'
urlpatterns = [
    path('add/', views.addBank, name='add' ),
    path('addProcss/', views.addBankProcss, name='addProcss' ),
    path('list/', views.banksList, name='list' ),
    path('<str:name>/modify/', views.modifyBank, name='modify' ),
    path('modifyProcess/', views.modifyBankProcess, name='modifyProcess' ),
]
