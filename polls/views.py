from django.http import HttpResponse
from django.shortcuts import render

def old_index(request):
    return HttpResponse("Hello, world, You're at the polls index.")

def index(request):
    context = {}
    return render(request, 'polls/index.html', context)
