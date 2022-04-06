from django.urls import path

from . import views

app_name = "travel"

urlpatterns = [
    path("user/company/", views.company_user, name="company_user"),
    path("company/", views.company, name="company"),
    # path("<slug:slug>", views.product_detail, name="product_detail"),
    # path("shop/<slug:category_slug>/", views.category_list, name="category_list"),
]
