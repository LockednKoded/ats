from django.shortcuts import render, redirect, get_object_or_404
from .models import ParkingSpot, VehicleDetail
from .forms import VehicleForm, ParkingForm

from django.core.exceptions import PermissionDenied
# Create your views here.


def parking_details(request):

    try:
        spots = ParkingSpot.objects.latest('last_updated')
    except (KeyError, ParkingSpot.DoesNotExist):
        return render(request, "parking/parking.html", {})

    return render(request, "parking/parking.html", {'spots': spots})


def update_spots(request):
    if request.user.is_superuser or request.user.is_staff:
        try:
            parking_instance = ParkingSpot.objects.latest('last_updated')
        except (KeyError, ParkingSpot.DoesNotExist):
            if request.method == "POST":
                form = ParkingForm(request.POST, request.FILES)

                if form.is_valid():
                    spots = form.save(commit=False)
                    spots.save()

                    return redirect("parking:details")
            else:
                form = ParkingForm()

            return render(request, 'parking/parking_form.html', {
                'title_message': 'Add Parking Slots',
                'submit_message': 'Add',
                'form': form,
            })
        if request.method == "POST":

            form = ParkingForm(request.POST, request.FILES, instance=parking_instance)
            if form.is_valid():
                spots = form.save(commit=False)
                spots.save()

                return redirect("parking:details")
        else:
            form = ParkingForm(instance=parking_instance)

        return render(request, 'parking/parking_form.html', {
            'title_message': 'Update Parking Spots',
            'submit_message': 'Update',
            'form': form,
        })

    else:
        raise PermissionDenied


def search_vehicle(request):

    if request.user.is_superuser or request.user.is_superuser:
        try:
            spots = ParkingSpot.objects.latest('last_updated')
            context = {'spots': spots}
        except (KeyError, ParkingSpot.DoesNotExist):
            context = {}
        try:
            query = request.GET.get('vno')
            if query != '\0':
                result = VehicleDetail.objects.get(vehicle_no=query)
                context.update({'result': result})
        except (KeyError, VehicleDetail.DoesNotExist):
                context.update({'no_match': 1})

        return render(request, 'parking/parking.html', context)

    else:
        raise PermissionDenied


def add_vehicle(request):
    if request.user.is_superuser or request.user.is_staff:
        if request.method == "POST":
            form = VehicleForm(request.POST, request.FILES)

            if form.is_valid():
                vehicle = form.save(commit=False)
                vehicle.save()

                return redirect("parking:details")
        else:
            form = VehicleForm()

        return render(request, 'parking/parking_form.html', {
            'title_message': 'Add new vehicle',
            'submit_message': 'Add',
            'form': form,
        })
    else:
        raise PermissionDenied


def delete_vehicle(request, pk):
    if request.user.is_superuser or request.user.is_staff:
        vehicle = get_object_or_404(VehicleDetail, vehicle_no=pk)
        vehicle.delete()
        return redirect("parking:details")
    else:
        raise PermissionDenied
