from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from ..models import Service,Travel
from ..forms import TravelForm
from django.contrib.auth.decorators import login_required
import datetime
@login_required
def add(request,service_id):
    service = get_object_or_404(Service,id=service_id)
    if request.method == "POST":
        form = TravelForm(request.POST, request.FILES)
        if form.is_valid():
            travel = form.save(commit=False)
            travel.available_seats = travel.passengers_limit
            travel.save()
            return HttpResponseRedirect(reverse("travel:service_detail" , kwargs={'slug':service.id}))
        else:
            return render(request, "travel/travel/add.html", {"form": form , "service":service})

    travel = Travel(
        service = service ,
        time_departure = datetime.date.today ,
        time_arrival_destination = datetime.date.today ,
        time_departure_return = datetime.date.today ,
        time_arrival_return =  datetime.date.today,
        travel_type = "V" ,
        passengers_limit = 100 ,
    )
    form = TravelForm(instance=travel)
    return render(request,"travel/travel/add.html",{"form": form , "service":service})

@login_required
def detail(request,slug,service_id):
    service = get_object_or_404(Service,id=service_id)
    travel = get_object_or_404(Travel,id=slug)
    return render(request,"travel/travel/detail.html",{"travel": travel,"service":service})



@login_required
def update(request,slug,service_id):
    service = get_object_or_404(Service,id=service_id)
    travel = get_object_or_404(Travel,id=slug,service=service)
    if request.method == "POST":
        form = TravelForm(request.POST, request.FILES,instance=travel)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("travel:travel_detail",kwargs={'slug':travel.id,'service_id':service.id }))
        else:
            return render(request,"travel/travel/update.html",{"form": form , "travel":travel,"service":service })
    form = TravelForm(instance=travel)
    return render(request,"travel/travel/update.html",{"form": form , "travel":travel,"service":service })


@login_required
def delete(request,slug,service_id):
    service = get_object_or_404(Service, id=service_id)
    travel = get_object_or_404(Travel, id=slug)
    if request.method == "POST":
        travel.delete()
        return render(request, "travel/travel/delete.html")
    return render(request, "travel/travel/delete.html", {"travel":travel,"service":service })



@login_required
def list(request):
    travels = Travel.objects.all().order_by("name")
    return render(request,"travel/travel/list.html",{"travels": travels})