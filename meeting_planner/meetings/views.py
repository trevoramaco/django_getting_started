from django.shortcuts import render, get_object_or_404, redirect
from .models import Meeting, Room

from django.forms import modelform_factory
from .forms import MeetingForm


# Create your views here.
def detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "meetings/detail.html", {"meeting": meeting})


def rooms(request):
    return render(request, "meetings/rooms.html", {"rooms": Room.objects.all()})


# Note: MeetingForm is a class! Not a regular object...
# MeetingForm = modelform_factory(Meeting, exclude=[])

def new(request):
    if request.method == "POST":
        # Form has been submitted, process data
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = MeetingForm()

    return render(request, "meetings/new.html", {"form": form})
