from django.shortcuts import render


def home(request):
    return render(request, 'site/home.html')


def about(request):
    return render(request, 'site/about.html')


def contact(request):
    return render(request, 'site/contact.html')


def faq(request):
    return render(request, 'site/freqQuest.html')


def toc(request):
    return render(request, 'site/toc.html')


def privacy(request):
    return render(request, 'site/privacyPolicy.html')

