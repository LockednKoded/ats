from django.shortcuts import render

# Create your views here.


def flight_details(request):
    return render(request, "flight_info/flight_info.html", {})
