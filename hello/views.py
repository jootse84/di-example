from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def image1(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'image1.html')


def image2(request):
    return render(request, 'image2.html')

