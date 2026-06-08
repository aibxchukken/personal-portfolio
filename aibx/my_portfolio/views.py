from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def skills(request):
    return render(request, 'skills.html')

def projects(request):
    return render(request, 'projects.html')

def certificates(request):
    return render(request, 'certificates.html')

def contact(request):
    return render(request, 'contact.html')