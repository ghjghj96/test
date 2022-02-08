from http.client import HTTPResponse
from mailbox import BabylMessage
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from banks.models import Bank

# Create your views here.

def addBank(request):
    return render(request, 'add.html')


def addBankProcss(request):
    name= request.POST.get('name')
    rate= request.POST.get('rate')
    
    qs=Bank(b_name=name, b_rate=rate)
    qs.save()
    
    return HttpResponseRedirect(reverse('index'))


def banksList(request):
    qs=Bank.objects.all()
    context={'banks':qs}
    return render(request, 'banksList.html',context)


def modifyBank(request,name):
    qs = Bank.objects.get(b_name=name)
    context= {'outcome':qs}
    return render(request, 'modify.html', context)
    
def modifyBankProcess(request):
    name= request.POST.get('name')
    rate= request.POST.get('rate')
    
    qs= Bank.objects.get(b_name=name)
    qs.b_name=name
    qs.b_rate=rate
    qs.save()
    return HttpResponseRedirect(reverse('index'))