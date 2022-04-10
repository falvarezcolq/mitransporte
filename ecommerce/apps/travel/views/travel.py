from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from ..models import Service
from ..forms import ServiceForm
from django.contrib.auth.decorators import login_required

@login_required
def add(request):
    if request.method == "POST":
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            service = form.save(commit=False)
            service.company = request.user.company
            service.save()
            return HttpResponseRedirect(reverse("travel:company_user"))
        else:
            return render(request, "travel/service/add.html", {"form": form})
    form = ServiceForm()
    return render(request,"travel/service/add.html",{"form": form})

@login_required
def detail(request,slug):
    service = get_object_or_404(Service,id=slug)
    return render(request,"travel/service/detail.html",{"service": service})



@login_required
def update(request,slug):

    service = get_object_or_404(Service,id=slug,company=request.user.company)
    if request.method == "POST":
        form = ServiceForm(request.POST, request.FILES,instance=service)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("travel:service_detail",kwargs={'slug':service.id}))
        else:
            return render(request, "travel/service/update.html", {"form": form , "service":service})
    form = ServiceForm(instance=service)
    return render(request,"travel/service/update.html",{"form": form , "service":service})


@login_required
def delete(request,slug):
    service = get_object_or_404(Service, id=slug)
    if request.method == "POST":
        service.delete()
        return render(request, "travel/service/delete.html")
    return render(request, "travel/service/delete.html", {"service":service})



@login_required
def list(request):
    services = Service.objects.all().order_by("name")
    return render(request,"travel/service/list.html",{"services": services})