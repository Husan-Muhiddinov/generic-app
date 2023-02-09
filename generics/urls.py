"""generics URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from employee.views import EmployeeCreate,EmployeeListView,EmployeeDetails,EmployeeUpdate,EmployeeDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',EmployeeCreate.as_view()),
    path('list/',EmployeeListView.as_view()),
    path('details/<pk>/',EmployeeDetails.as_view()),
    path('update/<pk>/',EmployeeUpdate.as_view()),
    path('delete/<pk>/',EmployeeDelete.as_view()),
]
