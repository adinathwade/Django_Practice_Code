from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def show(request):
    # return HttpResponse("from show....")
    # return HttpResponse("<h1>Hello i m fine</h1>")
    # a = "<h1>fine with django....</h1>"
    a=10+20
    return HttpResponse(a)
def test(request):
    return HttpResponse("from test....")