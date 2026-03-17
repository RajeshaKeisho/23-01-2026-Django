from django.urls import path 
from . import views

urlpatterns = [
    path("display/", views.display, name='display'),
    path("wish/", views.wish, name='wish'),
]




