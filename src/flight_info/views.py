from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from django.db.models import Q
from django.core.exceptions import PermissionDenied

from .models import Flight, Crew
from .forms import FlightForm, CrewForm


"""
    /////////////////////
        Flights views
    /////////////////////
"""


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


def get_days_field(days):

    if 'mon' in days:
        binary_days = '1,'
    else:
        binary_days = '0,'

    if 'tue' in days:
        binary_days += '1,'
    else:
        binary_days += '0,'

    if 'wed' in days:
        binary_days += '1,'
    else:
        binary_days += '0,'

    if 'thu' in days:
        binary_days += '1,'
    else:
        binary_days += '0,'

    if 'fri' in days:
        binary_days += '1,'
    else:
        binary_days += '0,'

    if 'sat' in days:
        binary_days += '1,'
    else:
        binary_days += '0,'

    if 'sun' in days:
        binary_days += '1'
    else:
        binary_days += '0'

    return binary_days


def add_flight(request):
    if request.user.is_superuser or request.user.is_superuser:
        if request.method == "POST":
            form = FlightForm(request.POST)

            if form.is_valid():
                flight = form.save(commit=False)

                days = form.cleaned_data.get('days_operational')
                binary_days = get_days_field(days)
                flight.operation_days = binary_days

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


"""
    /////////////////////
        Crew views
    /////////////////////
"""


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
    if request.user.is_superuser or request.user.is_staff:
        if request.method == "POST":
            form = CrewForm(request.POST, request.FILES)

            if form.is_valid():
                crew = form.save(commit=False)
                crew.flights = form.cleaned_data['flights']
                crew.save()

                return redirect("flight_info:list-crew")
        else:
            form = CrewForm()

        return render(request, 'flight_info/form.html', {
            'title_message': 'Add new crew',
            'submit_message': 'Add',
            'form':form,
        })
    else:
        raise PermissionDenied


def view_crew(request, pk):
    return HttpResponse("<h1>Details for " + pk + " crew</h1>")


def delete_crew(request, pk):
    if request.user.is_superuser or request.user.is_staff:
        crew = get_object_or_404(Crew, crew_id=pk)
        crew.delete()
        return redirect("flight_info:list-crew")
    else:
        raise PermissionDenied


def edit_crew(request, pk):
    if request.user.is_superuser or request.user.is_staff:
        crew_instance = get_object_or_404(Crew,crew_id=pk)
        if request.method == "POST":

            form = CrewForm(request.POST, request.FILES, instance=crew_instance)
            if form.is_valid():
                crew = form.save(commit=False)
                crew.flights = form.cleaned_data['flights']
                crew.save()

                return redirect("flight_info:list-crew")
        else:
            form = CrewForm(instance=crew_instance)

        return render(request, 'flight_info/form.html', {
            'title_message': 'Add new crew',
            'submit_message': 'Add',
            'form': form,
        })

    else:
        raise PermissionDenied


"""
    /////////////////////
        Airlines views
    /////////////////////
"""


def list_airlines(request):
    return HttpResponse("<h1>List of all airlines</h1>")


def add_airlines(request):
    return HttpResponse("<h1>Add a new airline</h1>")


def view_airlines(request,pk):
    return HttpResponse("<h1>Details for airline " + pk + "</h1>")


def delete_airlines(request,pk):
    return HttpResponse("<h1>Delete airline " + pk + "</h1>")


def edit_airlines(request,pk):
    return HttpResponse("<h1>Edit details of airline " + pk + "</h1>")