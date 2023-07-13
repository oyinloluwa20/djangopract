from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "boss/index.html")

def greet(request, name):
    return render(request, "boss/greet.html",{
        "namex": f"what the hell {name+1}"
    })




    