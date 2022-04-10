from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from ..models import Service,Travel
from ..forms import TravelForm
from django.contrib.auth.decorators import login_required


def home(request):
    services = Service.objects.all().order_by("name")
    return render(request,"public/travel/home.html",{"services": services})
