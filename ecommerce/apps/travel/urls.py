from django.urls import path

from .views import (
    company,
    places,
    service,
    travel,
    public,
)
app_name = "travel"

urlpatterns = [

    path("",public.home,name="home_travel"),
    path("travel/user/company/", company.company_user, name="company_user"),
    path("travel/company/",company.list,name="company_list"),
    path("travel/company/add/", company.add, name="company_add"),
    path("travel/company/update/<slug:slug>/", company.update, name="company_update"),
    path("travel/company/delete/<slug:slug>/", company.delete, name="company_delete"),
    path("travel/company/<slug:slug>/detail", company.detail, name="company_detail"),


    path("travel/places/add/", places.add, name="places_add"),
    path("travel/places/update/<slug:slug>/", places.update, name="places_update"),
    path("travel/places/delete/<slug:slug>/", places.delete, name="places_delete"),
    path("travel/places/",places.list,name="places_list"),
    path("travel/places/<slug:slug>/detail", places.detail, name="places_detail"),

    path("travel/service/add/", service.add, name="service_add"),
    path("travel/service/<slug:slug>/detail", service.detail, name="service_detail"),
    path("travel/service/update/<slug:slug>/", service.update, name="service_update"),
    path("travel/service/delete/<slug:slug>/", service.delete, name="service_delete"),
    path("travel/service/", service.list, name="service_list"),

    path("travel/service/<str:service_id>/travel/add/", travel.add, name="travel_add"),
    path("travel/service/<str:service_id>/travel/<slug:slug>/detail", travel.detail, name="travel_detail"),
    path("travel/service/<str:service_id>/travel/update/<slug:slug>/", travel.update, name="travel_update"),
    path("travel/service/<str:service_id>/travel/delete/<slug:slug>/", travel.delete, name="travel_delete"),
    path("travel/service/<str:service_id>/travel/", travel.list, name="travel_list"),

    # path("mycompany",views.CompanyView.as_view(),name="mycompany"),
    # path("<slug:slug>", views.product_detail, name="product_detail"),
    # path("shop/<slug:category_slug>/", views.category_list, name="category_list"),
]
