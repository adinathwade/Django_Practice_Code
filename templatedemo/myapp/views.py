from django.shortcuts import render

# Create your views here.
def home(request, a):

    print(a)
    r = {'my' : "my name is adi"}
    return render(request, 'myapp/home.html', context=r, content_type='text/html', status=None, using=None)