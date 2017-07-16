from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from django.db.models import Q
from django.core.exceptions import PermissionDenied

from .models import Flight, security_forces,  force_employee
from .forms import FlightForm, force_Form, AirlineForm


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
            Q(concourse__icontains=query)

        ).distinct()

    context = {
        'flight_list': queryset,
        'current_time': current_time,
    }
    return render(request, 'security_info/list_flights_.html', context)


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


def get_operation_days(days_binary_list):

    days_list = []

    if days_binary_list[0] == '1':
        days_list.append("Monday")

    if days_binary_list[1] == '1':
        days_list.append("Tuesday")

    if days_binary_list[2] == '1':
        days_list.append("Wedesday")

    if days_binary_list[3] == '1':
        days_list.append("Thursday")

    if days_binary_list[4] == '1':
        days_list.append("Friday")

    if days_binary_list[5] == '1':
        days_list.append("Saturday")

    if days_binary_list[6] == '1':
        days_list.append("Sunday")

    return days_list


def view_flight(request, pk):
    flight_instance = get_object_or_404(Flight, flight_no=pk)
    days_binary_list = flight_instance.operation_days.split(',')
    days_list = get_operation_days(days_binary_list)

    return render(request, 'security_info/detail_flights_.html', {
        'flight': flight_instance,
        'days': days_list,
    })


def delete_flight(request, pk):
    if request.user.is_superuser or request.user.is_staff:

        flight_instance = get_object_or_404(Flight, flight_no=pk)
        flight_instance_2 = get_object_or_404(Flight, flight_no=pk)  # need to fetch the instance twice, as one is del
        flight_instance.delete()
        return render(request, 'security_info/delete_flight_.html', {'flight': flight_instance_2})

    else:
        raise PermissionDenied


"""
    /////////////////////
        Crew views
    /////////////////////
"""


def list_force_employee(request):

    queryset = force_employee.objects.active()
    if request.user.is_superuser or request.user.is_staff:
        queryset = force_employee.objects.all()

    query = request.GET.get("q")
    if query:
        queryset = queryset.filter(
            Q(employee_id__icontains=query) |
            Q(name__icontains=query) |
            Q(flights__flight_no__icontains=query)
        ).distinct()

    return render(request, 'security_info/list_force_employee.html', {'crew_list': queryset, })


def add_force_employee(request):
    if request.user.is_superuser or request.user.is_staff:

        if request.method == "POST":
            form = force_Form(request.POST, request.FILES)  #

            if form.is_valid():
                crew = form.save(commit=False)
                crew.save()
                crew.flights = form.cleaned_data['flights']
                crew.save()

                return redirect("flight_info:view-crew", pk=crew.crew_id)
        else:
                form = force_Form()

        return render(request, 'security_info/form_1.html', {
            'title_message': 'Add new crew',
            'submit_message': 'Add',
            'form': form,
        })
    else:
        raise PermissionDenied


def edit_force_employee(request, pk):
    if request.user.is_superuser or request.user.is_staff:

        crew_instance = get_object_or_404(force_employee, employee_id=pk)
        if request.method == "POST":

            form = force_Form(request.POST, request.FILES, instance=crew_instance)
            if form.is_valid():
                crew = form.save(commit=False)
                crew.flights = form.cleaned_data['flights']
                crew.save()

                return redirect("security:view-force_employee", pk=force_employee.employee_id)
        else:
            form = force_Form(instance=crew_instance)

        return render(request, 'security_info/form_1.html', {
            'title_message': 'Add new crew',
            'submit_message': 'Add',
            'form': form,
        })

    else:
        raise PermissionDenied


def view_force_employee(request, pk):
    crew_instance = get_object_or_404(force_employee, employee_id=pk)
    return render(request, 'security_info/detail_force_employee.html', {'crew': crew_instance})


def delete_force_employee(request, pk):
    if request.user.is_superuser or request.user.is_staff:

        crew_instance = get_object_or_404(force_employee, employee_id=pk)
        crew_instance_2 = get_object_or_404(force_employee, employee_id=pk)
        crew_instance.delete()
        return render(request, 'security_info/delete_force_employee.html', {'crew': crew_instance_2})
    else:
        raise PermissionDenied















def list_security_forces(request):


    queryset = security_forces.objects.active()
    if request.user.is_staff or request.user.is_superuser:
        queryset = security_forces.objects.all()  # Show un-approved flights to authorised people

    query = request.GET.get("q")
    if query:
        queryset = queryset.filter(
            Q(name__icontains=query) |
            Q(license_no__icontains=query)

        ).distinct()




    return render(request, 'security_info/list_security_forces.html',{'security_forces_list': queryset, })



def add_security_forces(request):
    if request.user.is_superuser or request.user.is_superuser:

        if request.method == "POST":
            form = AirlineForm(request.POST)
            if form.is_valid():
                crew = form.save(commit=False)
                crew.save()
                crew.flights = form.cleaned_data['flights']
                crew.save()

                return redirect("security:view-security_forces", pk=crew.license_no)

        else:
            form = AirlineForm()

        return render(request, 'security_info/form_1.html', {
            'title_message': 'Add new security force',
            'submit_message': 'Add',
            'form': form,
        })

    else:
        raise PermissionDenied


def edit_security_forces(request, pk):
    if request.user.is_superuser or request.user.is_staff:

        crew_instance = get_object_or_404(security_forces, license_no=pk)
        if request.method == "POST":

            form = AirlineForm(request.POST, request.FILES, instance=crew_instance)
            if form.is_valid():
                crew = form.save(commit=False)
                crew.flights = form.cleaned_data['flights']
                crew.save()

                return redirect("security:view-security_forces", pk=crew.license_no)
        else:
            form = AirlineForm(instance=crew_instance)

        return render(request, 'security_info/form_1.html', {
            'title_message': 'Add new Security forces',
            'submit_message': 'Add',
            'form': form,
        })

    else:
        raise PermissionDenied

    def view_security_forces(request, pk):
        crew_instance = get_object_or_404(security_forces, license_no=pk)
        return render(request, 'security_info/detail_security_forces.html', {'crew': crew_instance})


def delete_security_forces(request, pk):
    if request.user.is_superuser or request.user.is_staff:

        crew_instance = get_object_or_404(security_forces, license_no=pk)
        crew_instance_2 = get_object_or_404(security_forces, license_no=pk)
        crew_instance.delete()
        return render(request, 'security_info/delete_security_forces.html', {'crew': crew_instance_2})
    else:
        raise PermissionDenied
