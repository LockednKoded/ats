from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.db.models import Q

from .forms import BaggageForm
from .models import BaggageHandling

def index(request):
    return render(request, 'baggage_handling/baggage_handling.html',{})

# detail view
def view_baggage(request,pk):
    baggage_instance = get_object_or_404(BaggageHandling, pk=pk)
    context = {'baggage': baggage_instance,}

    return render(request, 'baggage_handling/baggage_detail.html',context)



    return HttpResponse("Details for " + pk + "baggage")


def add_baggage(request):
    if request.user.is_superuser or request.user.is_superuser:
        if request.method == "POST":
            form = BaggageForm(request.POST)

            if form.is_valid():
                baggage = form.save(commit=False)

                baggage.save()

                return redirect("baggage_handling:list-baggage")
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
        return redirect("baggage_handling:list-baggage")
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

                return redirect("baggage_handling:list-baggage")
        else:
            form = BaggageForm(instance=baggage_instance)

        return render(request, 'baggage_handling/form.html', {
            'title_message': 'Edit baggage details',
            'submit_message': 'Save',
            'form': form,
        })
    else:
        raise PermissionDenied


def list_baggages(request):

    queryset = BaggageHandling.objects.all()

    query = request.GET.get("q")
    if query:
        queryset = queryset.filter(
            Q(pnr_no__icontains=query) |
            Q(quantity__icontains=query) |
            Q(weight__icontains=query) |
            Q(conveyor_no__icontains=query)
        ).distinct()

    context = {
        'baggage_list': queryset,
    }
    return render(request, 'baggage_handling/list_baggages.html', context)
