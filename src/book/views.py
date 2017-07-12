# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import generic
from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView,DeleteView

from .models import Album
from django.template import loader
from.forms import postform




# Create your views here.
from django.http import HttpResponse

def index(request):
    template=loader.get_template('book/index.html')
    return HttpResponse(template.render())


def post_create(request):
    form=postform
    MyProfileForm = postform(request.POST, request.FILES)

    if request.method=="POST":
        print request.POST.get("Room")
        print request.POST.get("duration")
        print request.POST.get("check_in")
        print request.POST.get("check_out")

    if MyProfileForm.is_valid():
        profile = Album()
        profile.Room = MyProfileForm.cleaned_data["Room"]
        profile.check_in = MyProfileForm.cleaned_data["check_in"]
        profile.check_out = MyProfileForm.cleaned_data["check_out"]
        profile.duration = MyProfileForm.cleaned_data["duration"]
        profile.save()
        saved = True

    context = {}
    return render(request, 'book/album_form.html', context)

def post_details(request):
    queryset=Album.objects.all()
    context={
        "object_list":queryset,
    }
    return render(request, 'book/data.html', context)
