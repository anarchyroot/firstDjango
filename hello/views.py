from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def say_hello(request):
    return render(request, 'index.html')


