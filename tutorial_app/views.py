from django.shortcuts import render
from .models import Message


def index(request):
    context = {
        'message': 'Hello'
    }
    return render(request, 'index.html', context)


def message(request, pk):
    context = {
        'message': Message.objects.get(pk=pk).content
    }
    return render(request, 'index.html', context)
