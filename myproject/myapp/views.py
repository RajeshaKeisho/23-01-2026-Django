# from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
# Create your views here.

def display(request):
    s = "<h1> Hello, Students! Welcome to Django Class!!</h1>"
    return HttpResponse(s)


def wish(request):
    current_time = timezone.now()
    hour = current_time.hour

    if 6 <= hour <= 12: 
        greeting_message = "Good Morning!"
    elif 12 <= hour <= 16:
        greeting_message = "Good Afternoon"
    elif 16 <= hour <= 21:
        greeting_message = "Good Evening"
    else:
        greeting_message = "Good Night"
    
    formatted_time = current_time.strftime("%d-%m-%Y %H:%M:%S")
    return HttpResponse(f"{greeting_message}! Today date and time is: {formatted_time}")


