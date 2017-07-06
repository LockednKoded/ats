from django.shortcuts import render
from django.http import HttpResponse

from .models import Cargo
# Create your views here.

def index(request):
    return render(request, "cargo/try1.html", {})


def view_cargo(request, pk):
    return HttpResponse("<h1>Details for Cargo Number" + pk +  "</h1>")