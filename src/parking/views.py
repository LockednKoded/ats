from django.shortcuts import render, render_to_response
from .models import ParkingSpot, VehicleDetail
# Create your views here.


def parking_details(request):

    try:
        spots = ParkingSpot.objects.latest('last_updated')
    except (KeyError, ParkingSpot.DoesNotExist):
        return render(request, "parking/parking.html", {})

    return render(request, "parking/parking.html", {'spots': spots})


def search(request):
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
