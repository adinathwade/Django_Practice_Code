from django.shortcuts import render

# Create your views here.
def test_home(request):
    return render(request, 'app/home.html')
def test_index(request):
    return render(request, 'app/index.html')