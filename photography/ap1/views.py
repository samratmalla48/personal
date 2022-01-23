from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
        return render(request,'ap1/index.html')
def first(request):
        return render(request,'ap1/firstpage.html')


