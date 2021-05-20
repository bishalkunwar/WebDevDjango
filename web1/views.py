from django.shortcuts import render

# Create your views here.

def homePageLanding(request):

    return render(request, 'web1/base.html')


def home(request):
    
    return render(request, 'web1/home.html')

def nav(request):

    return render(request, 'web1/navbar.html')