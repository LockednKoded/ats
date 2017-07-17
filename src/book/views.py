# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import generic
from django.shortcuts import render,redirect
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
    if request.method == "POST":
        form = postform(request.POST)

        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
            return redirect("book:listbookings")
    else:
        form = postform()
    context = {'form':postform}
    return render(request, 'book/album_form.html', context)

def post_details(request):
    queryset=Album.objects.all()
    context={
        "object_list":queryset,
    }
    return render(request, 'book/data.html', context)
