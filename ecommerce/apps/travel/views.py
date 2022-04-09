from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Company
from .forms import CompanyForm
from django.contrib.auth.decorators import login_required


@login_required
def company_user(request):
    try:
        company  = request.user.company
    except Company.DoesNotExist:
        company = None
    return render(request,"travel/company/company.html",{"company":company})



@login_required
def company(request):
    if request.method == "POST":
        company_form = CompanyForm(data=request.POST)
        if company_form.is_valid():
            company = company_form.save(commit=False)
            # import pdb;pdb.set_trace()
            company.user = request.user
            company.save()
            return HttpResponseRedirect(reverse("travel:company_user"))
        else:
            return render(request, "travel/company/company_create.html", {"form": company_form})

    company_form = CompanyForm()
    return render(request,"travel/company/company_create.html",{"form": company_form})


