from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse('Hello world')


def main_view(request):
    return render(request, 'main_view.html')