from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    return render(request, 'home.html')


@login_required
def about(request):
    return render(request, 'about.html')


def volunteer(request):
    return render(request, 'volunteer.html')


def contact(request):
    return render(request, 'contact.html')

