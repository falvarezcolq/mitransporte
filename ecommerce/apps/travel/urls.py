from django.urls import path

from .views import (
    company,
    places,
    service,
)
app_name = "travel"

urlpatterns = [
    path("user/company/", company.company_user, name="company_user"),
    path("company/",company.list,name="company_list"),
    path("company/add/", company.add, name="company_add"),
    path("company/update/<slug:slug>/", company.update, name="company_update"),
    path("company/delete/<slug:slug>/", company.delete, name="company_delete"),
    path("company/<slug:slug>/detail", company.detail, name="company_detail"),


    path("places/add/", places.add, name="places_add"),
    path("places/update/<slug:slug>/", places.update, name="places_update"),
    path("places/delete/<slug:slug>/", places.delete, name="places_delete"),
    path("places/",places.list,name="places_list"),
    path("places/<slug:slug>/detail", places.detail, name="places_detail"),

    path("service/add/", service.add, name="service_add"),
    path("service/<slug:slug>/detail", service.detail, name="service_detail"),
    path("service/update/<slug:slug>/", service.update, name="service_update"),
    path("service/delete/<slug:slug>/", service.delete, name="service_delete"),
    path("service/", service.list, name="service_list"),

    # path("mycompany",views.CompanyView.as_view(),name="mycompany"),
    # path("<slug:slug>", views.product_detail, name="product_detail"),
    # path("shop/<slug:category_slug>/", views.category_list, name="category_list"),
]
