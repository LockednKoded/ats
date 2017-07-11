from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from django.db.models import Q
from django.core.exceptions import PermissionDenied

from .models import Flight, Crew
from .forms import FlightForm


def list_flights(request):

    current_time = timezone.now()

    queryset = Flight.objects.active()
    if request.user.is_staff or request.user.is_superuser:
        queryset = Flight.objects.all()  # Show un-approved flights to authorised people

    query = request.GET.get("q")
    if query:
        queryset = queryset.filter(
            Q(airline__name__icontains=query) |
            Q(flight_no__icontains=query) |
            Q(destination__icontains=query) |
            Q(origin__icontains=query) |
            Q(terminal__icontains=query) |
            Q(concourse__icontains=query) |
            Q(revised_departure__icontains=query) |
            Q(revised_arrival__icontains=query)
        ).distinct()

    context = {
        'flight_list': queryset,
        'current_time': current_time,
    }
    return render(request, 'flight_info/list_flights.html', context)


def add_flight(request):
    if request.user.is_superuser or request.user.is_superuser:
        if request.method == "POST":
            form = FlightForm(request.POST)

            if form.is_valid():
                flight = form.save(commit=False)
                flight.save()

                return redirect("flight_info:list-flights")
        else:
            form = FlightForm()

        return render(request, 'flight_info/form.html', {
            'title_message': 'Add new flight',
            'submit_message': 'Add',
            'form': form,
        })

    else:
        raise PermissionDenied


def view_flight(request, pk):
    return HttpResponse("<h1>Details for " + pk + " flight</h1>")


def delete_flight(request, pk):
    if request.user.is_superuser or request.user.is_staff:
        flight = get_object_or_404(Flight, flight_no=pk)
        flight.delete()
        return redirect("flight_info:list-flights")
    else:
        raise PermissionDenied


def edit_flight(request, pk):
    if request.user.is_superuser or request.user.is_staff:
        flight_instance = get_object_or_404(Flight, flight_no=pk)
        if request.method == "POST":

            form = FlightForm(request.POST, instance=flight_instance)
            if form.is_valid():
                flight = form.save(commit=False)
                flight.save()

                return redirect("flight_info:list-flights")
        else:
            form = FlightForm(instance=flight_instance)

        return render(request, 'flight_info/form.html', {
            'title_message': 'Edit edit flight details',
            'submit_message': 'Save',
            'form': form,
        })
    else:
        raise PermissionDenied


def list_crew(request):
    queryset = Crew.objects.active()

    if request.user.is_superuser or request.user.is_staff:
        queryset = Crew.objects.all()

    query = request.GET.get("q")
    if query:
        queryset = queryset.filter(
            Q(crew_id__icontains=query) |
            Q(name__icontains=query) |
            Q(flights__flight_no__icontains=query)
        ).distinct()

    return render(request, 'flight_info/list_crew.html', {'crew_list': queryset, })


def add_crew(request):
    return HttpResponse("<h1>Add crew</h1>")


def view_crew(request, pk):
    return HttpResponse("<h1>Details for " + pk + " crew</h1>")


def delete_crew(request, pk):
    return HttpResponse("<h1>Delete " + pk + " crew</h1>")


def edit_crew(request, pk):
    return HttpResponse("<h1>Edit " + pk + " crew</h1>")