from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
    })


def search(request, name):
    return render(request, f'encyclopedia/{name}.html')
