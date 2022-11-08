from django.urls import path
from .views import CustomerListView, CustomerCreateView, CustomerUpdateView, CustomerDeleteView, CustomerList
from django.contrib.auth.decorators import login_required

app_name = "customer"
urlpatterns = [
    path("list/", login_required(CustomerListView.as_view()), name="customer-list"),
    path("", login_required(CustomerCreateView.as_view()), name="customer-create"),
    path("<int:id>/", login_required(CustomerUpdateView.as_view()), name="customer-update"),
    path("<int:id>/delete/", login_required(CustomerDeleteView.as_view()), name="customer-delete"),
    path("table/", login_required(CustomerList.as_view()), name="customer_table"),
]