from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'app/home.html', {'name' : 'adinath wade'}, content_type='text/html', status=None, using=None)
def index(request):
    return render(request, 'app/index.html')