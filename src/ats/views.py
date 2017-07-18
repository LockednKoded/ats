from django.shortcuts import render


def home_page(request):
    return render(request, 'common/home_page.html', {})


def contact_us(request):
    return render(request, 'common/contact_us.html', {})


def services(request):
    return render(request, 'common/services.html', {})


def developedby(request):
    return render(request, 'common/developedby.html', {})


def about_us(request):
    return render(request, 'common/about_us.html', {})
