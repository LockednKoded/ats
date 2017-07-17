from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from django.db.models import Q
from django.core.exceptions import PermissionDenied

from .models import  security_forces,  force_employee
from .forms import  force_Form, AirlineForm




"""
    /////////////////////
        Force employee  views
    /////////////////////
"""


def list_force_employee(request):

    queryset = force_employee.objects.all()

    # query = request.GET.get("q")
    # if query:
    #     queryset = queryset.filter(
    #         Q(employee_id__icontains=query) |
    #         Q(name__icontains=query) |
    #         Q(flights__flight_no__icontains=query)
    #     ).distinct()

    return render(request, 'security_info/list_force_employee.html', {'crew_list': queryset, })


def add_force_employee(request):
    if request.user.is_superuser or request.user.is_staff:

        if request.method == "POST":
            form = force_Form(request.POST, request.FILES)  #

            if form.is_valid():
                crew = form.save(commit=False)
                crew.save()
                #crew.flights = form.cleaned_data['flights']
                crew.save()

                return redirect("security:view-force_employee", pk=crew.employee_id)
        else:
                form = force_Form()

        return render(request, 'security_info/form_1.html', {
            'title_message': 'Add new Force employee',
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
                #crew.flights = form.cleaned_data['flights']
                crew.save()

                return redirect("security:view-force_employee", pk=force_employee.employee_id)
        else:
            form = force_Form(instance=crew_instance)

        return render(request, 'security_info/form_1.html', {
            'title_message': 'Edit Force employee',
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


    queryset = security_forces.objects.all()


   # query = request.GET.get("q")
    # if query:
    #     queryset = queryset.filter(
    #         Q(name__icontains=query) |
    #         Q(license_no__icontains=query)
    #
    #     ).distinct()




    return render(request, 'security_info/list_security_forces.html',{'security_forces_list': queryset, })



def add_security_forces(request):
    if request.user.is_superuser or request.user.is_superuser:

        if request.method == "POST":
            form = AirlineForm(request.POST)
            if form.is_valid():
                crew = form.save(commit=False)
                crew.save()
                #crew.flights = form.cleaned_data['flights']
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
                #crew.flights = form.cleaned_data['flights']
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
