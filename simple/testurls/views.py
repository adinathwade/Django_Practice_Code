from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def display(request, pk='hi', **kwargs):
    print(kwargs, pk)
    return HttpResponse("from display testing...")
