from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_page(request):

    # contexto
    context = {
        "message": "This is a message!",
    }

    return render(request, "home_page.html", context)