from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from ..models import Place
from ..forms import PlaceForm
from django.contrib.auth.decorators import login_required

@login_required
def add(request):
    if request.method == "POST":
        place_form = PlaceForm(request.POST, request.FILES)
        if place_form.is_valid():
            place_form.save()
            return HttpResponseRedirect(reverse("travel:places_list"))
        else:
            return render(request, "travel/places/add.html", {"form": place_form})
    place_form = PlaceForm()
    return render(request,"travel/places/add.html",{"form": place_form})


@login_required
def update(request,slug=None):
    place = get_object_or_404(Place, id=slug)
    if request.method == "POST":
        place_form = PlaceForm(data=request.POST,files=request.FILES,instance=place)
        if place_form.is_valid():
            place_form.save()
            return HttpResponseRedirect(reverse("travel:places_list"))
        else:
            return render(request,"travel/places/update.html",{"form": place_form ,'place':place})

    place_form = PlaceForm(instance=place)
    return render(request,"travel/places/update.html",{"form": place_form ,'place':place})

@login_required
def detail(request,slug):
    place = get_object_or_404(Place, id=slug)
    return render(request, "travel/places/detail.html", {"place": place})


@login_required
def delete(request,slug):
    place = get_object_or_404(Place, id=slug)
    if request.method == "POST":
        place.delete()
        return render(request,"travel/places/delete.html")
    return render(request, "travel/places/delete.html", {"place":place})


@login_required
def list(request):
    places = Place.objects.all().order_by("name")
    return render(request,"travel/places/list.html",{"places": places})
