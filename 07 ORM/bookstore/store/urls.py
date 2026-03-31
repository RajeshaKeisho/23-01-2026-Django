from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='books'),
    path('dashboard', views.sales_dashboard, name='dashbaord'),
    path('rawsql', views.raw_sql_view, name='rawsql'),
]