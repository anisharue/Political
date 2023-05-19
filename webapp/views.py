from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home(request):
    """
    View function for the home page of the website.

    :param request: the HTTP request object
    :return: a rendered response for the home page template
    """
    return render(request, 'home.html')


@login_required
def about(request):
    """
    View function for the about page of the website, which requires
    authentication.

    :param request: the HTTP request object
    :return: a rendered response for the about page template
    """
    return render(request, 'about.html')


def volunteer(request):
    """
    View function for the volunteer page of the website.

    :param request: the HTTP request object
    :return: a rendered response for the volunteer page template
    """
    return render(request, 'volunteer.html')


def contact(request):
    """
    View function for the contact page of the website.

    :param request: the HTTP request object
    :return: a rendered response for the contact page template
    """
    return render(request, 'contact.html')


