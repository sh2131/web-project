from django.shortcuts import render, HttpResponse

# Create your views here.



def home(request):
   templates = loader.get_template("home.html")
    return HttpResponse(templates.render())



