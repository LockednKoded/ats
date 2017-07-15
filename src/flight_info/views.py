from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from django.db.models import Q
from django.core.exceptions import PermissionDenied

from .models import Flight, Crew,  Airline
from .forms import FlightForm, CrewForm, AirlineForm


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

                return redirect("flight_info:view-flight", pk=flight.flight_no)
        else:
            form = FlightForm()

        return render(request, 'flight_info/form.html', {
            'title_message': 'Add new flight',
            'submit_message': 'Add',
            'form': form,
        })

    else:
        raise PermissionDenied


def edit_flight(request, pk):
    if request.user.is_superuser or request.user.is_staff:

        flight_instance = get_object_or_404(Flight, flight_no=pk)
        if request.method == "POST":

            form = FlightForm(request.POST, instance=flight_instance)
            if form.is_valid():
                flight = form.save(commit=False)

                days = form.cleaned_data.get('days_operational')
                binary_days = get_days_field(days)
                flight.operation_days = binary_days

                flight.save()

                return redirect("flight_info:view-flight", pk=flight.flight_no)
        else:
            form = FlightForm(instance=flight_instance)

        return render(request, 'flight_info/form.html', {
            'title_message': 'Edit flight details',
            'submit_message': 'Save',
            'form': form,
        })
    else:
        raise PermissionDenied


def view_flight(request, pk):
    flight_instance = get_object_or_404(Flight, flight_no=pk)
    return render(request, 'flight_info/detail_flights.html', {'flight': flight_instance})


def delete_flight(request, pk):
    if request.user.is_superuser or request.user.is_staff:

        flight_instance = get_object_or_404(Flight, flight_no=pk)
        flight_instance_2 = get_object_or_404(Flight, flight_no=pk)  # need to fetch the instance twice, as one is del
        flight_instance.delete()
        return render(request, 'flight_info/delete_flight.html', {'flight': flight_instance_2})

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

                return redirect("flight_info:view-crew", pk=crew.crew_id)

            form = CrewForm()

        return render(request, 'flight_info/form.html', {
            'title_message': 'Add new crew',
            'submit_message': 'Add',
            'form': form,
        })
    else:
        raise PermissionDenied


def edit_crew(request, pk):
    if request.user.is_superuser or request.user.is_staff:

        crew_instance = get_object_or_404(Crew, crew_id=pk)
        if request.method == "POST":

            form = CrewForm(request.POST, request.FILES, instance=crew_instance)
            if form.is_valid():
                crew = form.save(commit=False)
                crew.flights = form.cleaned_data['flights']
                crew.save()

                return redirect("flight_info:view-crew", pk=crew.crew_id)
        else:
            form = CrewForm(instance=crew_instance)

        return render(request, 'flight_info/form.html', {
            'title_message': 'Add new crew',
            'submit_message': 'Add',
            'form': form,
        })

    else:
        raise PermissionDenied


def view_crew(request, pk):
    return HttpResponse("<h1>Details for " + pk + " crew</h1>")


def delete_crew(request, pk):
    if request.user.is_superuser or request.user.is_staff:

        crew_instance = get_object_or_404(Crew, crew_id=pk)
        crew_instance.delete()
        return redirect("flight_info:list-crew")
    else:
        raise PermissionDenied


"""
    /////////////////////
        Airlines views
    /////////////////////
"""


def list_airlines(request):
    queryset = Airline.objects.all()

    query = request.GET.get("q")
    if query:
        queryset = queryset.filter(
            Q(name__icontains=query) |
            Q(flight_prefix__icontains=query) |
            Q(license_no__icontains=query) |
            Q(no_of_aircrafts__icontains=query)
        ).distinct()

    context = {
        'airline_list': queryset
    }
    return render(request, 'flight_info/list_airlines.html', context)


def add_airlines(request):
    if request.user.is_superuser or request.user.is_staff:
        if request.method == "POST":
            form = AirlineForm(request.POST)

            if form.is_valid():
                airline = form.save(commit=False)

                airline.save()

                return redirect("flight_info:view-airlines", pk=airline.flight_prefix)
                # return redirect("flight-info:list-airlines", )
        else:
            form = AirlineForm()

        return render(request, 'flight_info/form.html', {
            'title_message': 'Add new Airline',
            'submit_message': 'Add',
            'form': form,
        })
    else:
        raise PermissionDenied



def edit_airlines(request, pk):
    return HttpResponse("<h1>Edit details of airline " + pk + "</h1>")


def view_airlines(request, pk):
    airline_instance = get_object_or_404(Airline, flight_prefix=pk)
    return render(request, 'flight_info/detail_airline.html', {'airline': airline_instance})


def delete_airlines(request, pk):
    return HttpResponse("<h1>Delete airline " + pk + "</h1>")