from django.shortcuts import render

# Create your views here.
from .models import Employee

def employee_view(request):
    emp_data = Employee.objects.all()
    my_dict = {'emp_data':emp_data}
    return render(request, 'home.html', context=my_dict)