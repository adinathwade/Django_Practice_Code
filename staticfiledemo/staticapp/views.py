from django.shortcuts import render

# Create your views here.
def static_home(request):
    return render(request, 'home.html')
