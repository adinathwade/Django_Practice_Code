from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
# Create your views here.
class ViewClass(View):
    def get(self, request):
        return HttpResponse("from class view....")

def detail(request, question_id):

    return HttpResponse("You're looking at question %s." % question_id)

def result(request, question_id):
    return HttpResponse("You're looking at the results of question %s."% question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
