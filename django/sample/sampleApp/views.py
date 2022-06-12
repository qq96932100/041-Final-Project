from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.
def sayhello(request):
    return HttpResponse("Hello")
def index(request):
    now = datetime.now()
    return render(request,"index.html",locals())