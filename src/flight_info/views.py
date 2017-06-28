from django.shortcuts import render
from django.http import HttpResponse

from .models import Flight, Crew

# Create your views here.


def list_flights(request):
    return HttpResponse("<h1>Flights list</h1>")


def add_flight(request):
    return HttpResponse("<h1>Add flight</h1>")


def view_flight(request, pk):
    return HttpResponse("<h1>Details for " + pk + " flight</h1>")


def delete_flight(request, pk):
    return HttpResponse("<h1>Delete " + pk + " flight</h1>")


def edit_flight(request, pk):
    return HttpResponse("<h1>Edit " + pk + " flight</h1>")


def list_crew(request):
    return HttpResponse("<h1>Crew list</h1>")


def add_crew(request):
    return HttpResponse("<h1>Add crew</h1>")


def view_crew(request, pk):
    return HttpResponse("<h1>Details for " + pk + " crew</h1>")


def delete_crew(request, pk):
    return HttpResponse("<h1>Delete " + pk + " crew</h1>")


def edit_crew(request, pk):
    return HttpResponse("<h1>Edit " + pk + " crew</h1>")