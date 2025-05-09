from django.shortcuts import render
from django.http import Http404

def home(request):
    try:
        return render(request, "home.html")
    except TemplateDoesNotExist:
        raise Http404("Template not found")

def about(request):
    try:
        return render(request, "about.html")
    except TemplateDoesNotExist:
        raise Http404("Template not found")

def contact(request):
    try:
        return render(request, "contact.html")
    except TemplateDoesNotExist:
        raise Http404("Template not found")

def services(request):
    try:
        return render(request, "services.html")
    except TemplateDoesNotExist:
        raise Http404("Template not found")

def portfolio(request):
    try:
        return render(request, "portfolio.html")
    except TemplateDoesNotExist:
        raise Http404("Template not found")
