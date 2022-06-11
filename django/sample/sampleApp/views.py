from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.
def sayhello(request):
    return HttpResponse("Hello")
def templates(request):
    now = datetime.now()
    return render(request,"Hello.html",locals())