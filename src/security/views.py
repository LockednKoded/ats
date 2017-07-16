from django.shortcuts import render
from django.http import HttpResponse

from .models import Flight, force_employee

# Create your views here.


def list_flights(request):
    return HttpResponse("<h1>Flights list</h1>")


def view_flight(request, pk):
    return HttpResponse("<h1>Details for " + pk + " flight</h1>")


def list_force_employee(request):
    return HttpResponse("<h1>Force employee list</h1>")


def add_force_employee(request):
    return HttpResponse("<h1>Add Force employee</h1>")


def view_force_employee(request, pk):
    return HttpResponse("<h1>Details for " + pk + " Force employee</h1>")


def delete_force_employee(request, pk):
    return HttpResponse("<h1>Delete " + pk + " Force employee</h1>")


def edit_force_employee(request, pk):
    return HttpResponse("<h1>Edit " + pk + " Force employee</h1>")