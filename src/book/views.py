# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import Book
from .forms import postform


# Create your views here.


def index(request):
    return render(request, 'book/index.html', {})


def post_create(request):
    if request.method == "POST":
        form = postform(request.POST)

        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
            return redirect("book:listbookings")
    else:
        form = postform()
    context = {'form': form}
    return render(request, 'book/album_form.html', context)


def post_details(request):
    queryset = Book.objects.all()
    context = {
        "object_list": queryset,
    }
    return render(request, 'book/data.html', context)
