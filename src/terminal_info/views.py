from django.shortcuts import render

# Create your views here.


def terminal_info(request):
    return render(request, "terminal_info/terminal.html", {})


def terminal_1_view(request):
    return render(request, "terminal_info/terminal_1.html", {})

def terminal_1_view_1(request):
    return render(request, "terminal_info/terminal_3.html", {})