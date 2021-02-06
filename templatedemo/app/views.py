from django.shortcuts import render

# Create your views here.
def home(request):
    return  render(request, 'app/home.html', {'message':'good day'}, content_type='text/html')