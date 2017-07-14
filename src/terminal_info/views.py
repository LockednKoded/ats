from django.shortcuts import render

# Create your views here.


def terminal_info(request):
    return render(request, "terminal_info/terminal_info.html", {})
