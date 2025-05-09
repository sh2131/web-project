from django.shortcuts import render


from django.template import loader
from django.http import HttpResponse

def home(request):
    templates = loader.get_template("home.html")
    return HttpResponse(templates.render())




