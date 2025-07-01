from django.shortcuts import render
from django.core.mail import send_mail
from .models import Project

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def projects(request):
    all_projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': all_projects})

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        send_mail(
            f"Contact Form Message from {name}",
            message,
            email,
            ['your@email.com'],
        )
    return render(request, 'contact.html')
