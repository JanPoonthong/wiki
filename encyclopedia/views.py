from django.shortcuts import render
from django import forms
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.forms import Form

from . import util
from markdown2 import Markdown
import secrets


class EditForm(forms.Form):
    title = forms.CharField(label="Entry title", widget=forms.TextInput(attrs={'class': 'form-control col-md-8 col-lg-8'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control col-md-8 col-lg-8', 'rows': 10}))
    edit = forms.BooleanField(initial=False, widget=forms.HiddenInput(), required=False)

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
        form.fields["title"].initial = edit_entry
        form.fields["title"].widget = forms.HiddenInput()
        form.fields["content"].initial = content
        form.fields["edit"].initial = True
        return render(request, "encyclopedia/newentry.html", {
            "form": form,
            "edit": form.fields["edit"].initial,
            "title": form.fields["title"].initial
        })
    else:
        return render(request, "encyclopedia/nonexistingentry.html", {
            "title": edit_entry
        })

def newentry(request):
    if request.method == "POST":
        form = EditForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            if util.get_entry(title) is None or form.cleaned_data["edit"] is True:
                util.save_entry(title, content)
                return HttpResponseRedirect(reverse("entry", kwargs={'entry_title': title}))
            else:
                return render(request, "encyclopedia/newentry.html", {
                    "form": form,
                    "entry_title": title
                })
        else:
            return render(request, "encyclopedia/newentry.html", {
                "form": form,
            })
    else:
        return render(request, "encyclopedia/newentry.html", {
            "form": EditForm(),
        })

def random(request):
    entries = util.list_entries()
    random_entry = secrets.choice(entries)
    return HttpResponseRedirect(reverse("entry", kwargs={'entry_title': random_entry}))

def search(request):
    value = request.GET.get('q', '')
    if util.get_entry(value) is not None:
        return HttpResponse(reverse("entry", kwargs={'entry_title': value}))
    else:
        sub_string_entries = []
        for entry in util.list_entries():
            if value.upper() in entry.upper():
                sub_string_entries.append(entry)
        return render(request, "encyclopedia/index.html", {
            "entries": sub_string_entries,
            "search": True,
            "value": value
        })