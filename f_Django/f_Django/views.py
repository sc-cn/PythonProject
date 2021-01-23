from django.shortcuts import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello(request):
    return HttpResponse("hello world!!!")

def index(request):
    return render(request,"index.html")

