from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Contact


def say_hello(request):
    contacts = Contact.objects.all()
    return render(request, 'index.html', {'contacts': contacts})
