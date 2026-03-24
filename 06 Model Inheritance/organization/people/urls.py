from django.urls import path
from .views import EmployeeListView, CustomerListView

urlpatterns = [
    path('employees/', EmployeeListView.as_view(), name='employees'),
    path('customers/', CustomerListView.as_view(), name='customers'),
]