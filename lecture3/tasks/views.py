from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


# Create your views here.
class NewTaskForm(forms.Form):
    task = forms.CharField(label = 'New Task')


# listing the tasks

def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })


def add(request):
    #check for both server and client side validation
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"].append(task)
            request.session.modified = True  # Ensure the session is saved after modification
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, 'tasks/add.html', {"form": form})


    return render(request, 'tasks/add.html', {
        "form": NewTaskForm()
    })

