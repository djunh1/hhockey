from django.shortcuts import render

def home(request):
    return render(request, 'site/home.html')


def about(request):
    return render(request, 'site/about.html')


def contact(request):
    return render(request, 'site/contact.html')

