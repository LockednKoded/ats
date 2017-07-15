from django.shortcuts import render

# Create your views here.


def parking_details(request):
    return render(request, "security/security.html", {})