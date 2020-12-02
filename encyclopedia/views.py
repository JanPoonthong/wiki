from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
    })


def Django(request):
    return render(request, 'encyclopedia/django.html')


def CSS(request):
    return render(request, 'encyclopedia/css.html')


def Git(request):
    return render(request, 'encyclopedia/git.html')


def HTML(request):
    return render(request, 'encyclopedia/HTML.html')


def Python(request):
    return render(request, 'encyclopedia/python.html')
