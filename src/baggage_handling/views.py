from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import PermissionDenied
from .forms import BaggageForm
from .models import BaggageHandling

def index(request):
    return render(request, 'baggage_handling/baggage_handling.html',{})



def add_baggage(request):
    if request.user.is_superuser or request.user.is_superuser:
        if request.method == "POST":
            form = BaggageForm(request.POST)

            if form.is_valid():
                baggage = form.save(commit=False)

                baggage.save()

                return redirect("baggage_handling:index")
        else:
            form = BaggageForm()

        return render(request, 'baggage_handling/form.html', {
            'title_message': 'Add new baggage',
            'submit_message': 'Add',
            'form': form,
        })

    else:
        raise PermissionDenied


def delete_baggage(request, pk):
    if request.user.is_superuser or request.user.is_staff:
        baggage = get_object_or_404(BaggageHandling, pk=pk)
        baggage.delete()
        return redirect("baggage_handling:index")
    else:
        raise PermissionDenied


def edit_baggage(request, pk):
    if request.user.is_superuser or request.user.is_staff:
        baggage_instance = get_object_or_404(BaggageHandling, pk=pk)
        if request.method == "POST":

            form = BaggageForm(request.POST, instance=baggage_instance)
            if form.is_valid():
                baggage = form.save(commit=False)
                baggage.save()

                return redirect("baggage_handling:index")
        else:
            form = BaggageForm(instance=baggage_instance)

        return render(request, 'baggage_handling/form.html', {
            'title_message': 'Edit edit baggage details',
            'submit_message': 'Save',
            'form': form,
        })
    else:
        raise PermissionDenied



