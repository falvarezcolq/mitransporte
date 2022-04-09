from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from ..models import Company
from ..forms import CompanyForm
from django.contrib.auth.decorators import login_required
from django.views import View


from django.http import HttpResponse
@login_required
def company_user(request):
    try:
        company  = request.user.company
        return render(request, "travel/company/company.html", {"company": company})
    except Company.DoesNotExist:
        company = None
    company = None
    return render(request, "travel/company/company.html", {"company": False})


@login_required
def add(request):
    if request.method == "POST":
        company_form = CompanyForm(data=request.POST)
        if company_form.is_valid():
            company = company_form.save(commit=False)
            company.user = request.user
            company.save()
            return HttpResponseRedirect(reverse("travel:company_user"))
        else:
            return render(request, "travel/company/add.html", {"form": company_form})
    company_form = CompanyForm()
    return render(request,"travel/company/add.html",{"form": company_form})


@login_required
def update(request,slug=None):
    company = get_object_or_404(Company, id=slug)
    if request.method == "POST":
        company_form = CompanyForm(data=request.POST,instance=company)
        if company_form.is_valid():
            company_form.save()
            return HttpResponseRedirect(reverse("travel:company_user"))
        else:
            return render(request,"travel/company/update.html",{"form": company_form ,'company':company})

    company_form = CompanyForm(instance=company)
    return render(request,"travel/company/update.html",{"form": company_form ,'company':company})

@login_required
def detail(request,slug):
    company = get_object_or_404(Company, id=slug)
    return render(request, "travel/company/company.html", {"company": company})


@login_required
def delete(request,slug):
    company = get_object_or_404(Company, id=slug)
    if request.method == "POST":
        company.delete()
        return render(request,"travel/company/delete.html")
    return render(request, "travel/company/delete.html", {"company":company})


@login_required
def list(request):
    companies = Company.objects.all().order_by("name")
    return render(request,"travel/company/list.html",{"companies": companies})
