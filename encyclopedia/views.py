from django.shortcuts import render
from django import forms

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
    })


def entry(request, entry_title):
    entry_title = entry_title.lower()
    try:
        return render(request, f"encyclopedia/{entry_title}.html")
    except:
        return render(request, "encyclopedia/error.html", {
            "title": entry_title
        })


def edit_page(request, edit_title):
    content = util.get_entry(edit_title)
    return render(request, "encyclopedia/edit.html", {
        "page_title": edit_title,
        "content": content
    })
