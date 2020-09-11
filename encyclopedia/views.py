from django.shortcuts import render
from markdown import markdown
from . import util
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from encyclopedia.forms import NewPageForm, EditEntryForm
import random

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "header": "All pages"
    })

def title(request, entry_name):
    if util.get_entry(entry_name) is not None:
        return render(request, "encyclopedia/entry.html", {
        "entry": markdown(util.get_entry(entry_name)),
        "title": entry_name
    })
    else:
        return render(request, "encyclopedia/errors.html", {
        "message": " Page dose not exists" 
    })


def search(request):
    query =  request.POST.get('key_words')
    if query in util.list_entries():
        return render(request, "encyclopedia/entry.html", {
        "entry": markdown(util.get_entry(query)),
        "title": query })
    else:
        lst_of_results= [i for i in util.list_entries()  if query in i]
        return render(request, "encyclopedia/index.html", {
            "entries": lst_of_results,
            "header": "All search results"
    })

def New_Page(request):
    if request.method == 'POST':
        form = NewPageForm(request.POST)
        title   = request.POST.get('title')
        content = request.POST.get('content')
        if form.is_valid():
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse('title', args=[title]) )
    else:
        return render(request, "encyclopedia/new_page.html")


def Edit_Page(request, name):
    form = EditEntryForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            util.save_entry(title,content)
        return HttpResponseRedirect(reverse('title', args=[title]) )

    if request.method =="GET":
        return render(request, "encyclopedia/edit.html", {
        "form": EditEntryForm(name),
        "title": name,
        "content": markdown(util.get_entry(name))
         })
         
def Random_Page(request):
    random_pagename = random.choice(util.list_entries())
    return HttpResponseRedirect(reverse('title', args=[random_pagename]) )
