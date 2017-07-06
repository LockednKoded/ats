from django.shortcuts import render
from django.http import HttpResponse


def test_view(request):
    return HttpResponse("<h2>Maintenance view is working</h2>")