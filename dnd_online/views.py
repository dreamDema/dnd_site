from django.shortcuts import render

def index(request):
    return render(request, 'dnd_online/homePage.html')

def page_not_found(request, exeption):
    return render(request, 'dnd_online/404.html')