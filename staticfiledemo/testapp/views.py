from django.shortcuts import render

# Create your views here.
def static_inapp(request):
    return render(request, 'index.html')