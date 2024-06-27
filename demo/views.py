from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
# when i call localhost:8000/demo/hello, i want

def say_hello(request):
    return HttpResponse("Welcome to django")


def welcome(request, name):
    return render(request, "index.html", context={"name": name })
