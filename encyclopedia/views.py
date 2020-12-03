from django.shortcuts import render
from django import forms
from django.http import HttpResponse
from django.forms import Form

from . import util
from markdown2 import Markdown


class EditForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control col-md-8 col-lg-8', 'rows' : 10}))


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
    })


def entry(request, entry_title):
    content = util.get_entry(entry_title)
    if content is not None:
        return render(request, "encyclopedia/entry.html", {
            "content": Markdown().convert(content),
            "title": entry_title
        })
    else:
        return render(request, "encyclopedia/nonexistingentry.html", {
            "title": entry_title
        })

def edit(request, edit_entry):
    content = util.get_entry(edit_entry)
    if content is not None:
        form = EditForm()
        form.fields["content"].initial = content
        return render(request, "encyclopedia/edit_entry.html", {
            "form": form,
            "title": edit_entry,
            "content": content
        })