from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
    })


def search(request, name):
    try:
        return render(request, f"encyclopedia/{name}.html")
    except:
        return render(request, "encyclopedia/error.html")


def edit_page(request, edit_title):
    content = util.get_entry(edit_title)
    return render(request, "encyclopedia/edit.html", {
        "page_title": edit_title,
        "content": content
    })
