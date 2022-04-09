from django.urls import path

from .views import (
    company
)
app_name = "travel"

urlpatterns = [
    path("user/company/", company.company_user, name="company_user"),
    path("company/",company.list,name="company_list"),
    path("company/add/", company.add, name="company_add"),
    path("company/update/<slug:slug>/", company.update, name="company_update"),
    path("company/delete/<slug:slug>/", company.delete, name="company_delete"),
    path("company/<slug:slug>/detail", company.detail, name="company_detail"),
    # path("mycompany",views.CompanyView.as_view(),name="mycompany"),
    # path("<slug:slug>", views.product_detail, name="product_detail"),
    # path("shop/<slug:category_slug>/", views.category_list, name="category_list"),
]
