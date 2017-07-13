from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'baggage_handling/baggage_handling.html',{})