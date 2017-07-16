from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.db.models import Q
from django.core.exceptions import PermissionDenied
from .models import cargo

from .forms import CargoForm
# Create your views here.


def list_cargo(request):

    current_time = timezone.now()

    queryset = cargo.objects.active()
    if request.user.is_staff or request.user.is_superuser:
        queryset = cargo.objects.all()  # Show un-approved flights to authorised people

    query = request.GET.get("q")
    if query:
        queryset = queryset.filter(
            Q(cargo_no__icontains=query) |
            Q(cargo_airline__icontains=query) |
            Q(destination__icontains=query) |
            Q(terminal__icontains=query) |
            Q(fare__icontains=query) |
            Q(scheduled_departure__icontains=query)
        ).distinct()

    context = {
        'cargo_list': queryset,
        'current_time': current_time,
    }
    return render(request, 'cargo/form.html', context)


def add_cargo(request):
    if request.user.is_staff or request.user.is_superuser:
        if request.method == "POST":
            form = CargoForm(request.POST)

            if form.is_valid():
                # flight = form.save(commit=False)
                # flight.save()
                cargo = form.save(commit=True)

                return render(request, "cargo/book_done.html", {})
               # return redirect("cargo:try1")
        else:
            form = CargoForm()

        return render(request, 'cargo/form.html', {
            'title_message': 'Add new Cargo',
            'submit_message': 'Add',
            'form': form,
        })

    else:
        raise PermissionDenied



def delete_cargo(request, pk):
    if request.user.is_superuser or request.user.is_staff:
        cargo = get_object_or_404(cargo, cargo_no=pk)
        cargo.delete()
        return redirect("cargo:list-cargo")
    else:
        raise PermissionDenied



def index(request):
    return render(request, "cargo/try1.html", {})

def disclaimer(request):
    return render(request, "cargo/disclaimer.html", {})

def helpandsupport(request):
    return render(request, "cargo/helpandsupport.html", {})


def faq(request):
    return render(request, "cargo/faq.html", {})

def guideline(request):
    return render(request, "cargo/guideline.html", {})

def procedure(request):
    return render(request, "cargo/procedure.html", {})


def cargolist(request):
    return render(request, "cargo/list_cargo.html", {})


def faretable(request):
    return render(request, "cargo/faretable.html", {})


def export(request):
    return render(request, "cargo/export.html", {})



def aboutus(request):
    return render(request, "cargo/aboutus.html", {})

def bookcargo(request):
    return render(request, "cargo/form.html", {})

def view_cargo(request,pk):
    return render(request, "cargo/layout.html", {})
   # return HttpResponse("<h1>Details for Cargo Number" + pk +  "</h1>")


def edit_cargo(request, pk):
    if request.user.is_superuser or request.user.is_staff:
        cargo_instance = get_object_or_404(cargo, cargo_no=pk)
        if request.method == "POST":

            form = CargoForm(request.POST, instance=cargo_instance)
            if form.is_valid():
                flight = form.save(commit=False)
                flight.save()
                return render(request, "cargo/try1.html", {})

        else:
            form = CargoForm(instance=cargo_instance)

        return render(request, 'cargo/form.html', {
            'title_message': 'Edit edit cargo details',
            'submit_message': 'Save',
            'form': form,
        })
    else:
        raise PermissionDenied

def delete_cargo(request, pk):
    if request.user.is_superuser or request.user.is_staff:
        Cargo = get_object_or_404(cargo, cargo_no=pk)
        Cargo.delete()
        return render(request, "cargo/form.html", {})
    else:
        raise PermissionDenied