from django.shortcuts import render
from .models import Employee
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.


class EmployeeCreate(CreateView):
    model=Employee
    template_name='employee_form.html'
    fields="__all__"
    success_url="/list"


class EmployeeListView(ListView):
    template_name="employee_list.html"
    model=Employee
    def get_queryset(self):
        qs=Employee.objects.all()
        return qs
    

class EmployeeDetails(DetailView):
    model=Employee
    template_name='employee_Detail.html'


class EmployeeUpdate(UpdateView):
    model=Employee
    template_name='employee_form.html'
    fields="__all__"
    success_url="/list"

class EmployeeDelete(DeleteView):
    model=Employee
    template_name='employee_confirm_delete.html'
    success_url="/list"
    