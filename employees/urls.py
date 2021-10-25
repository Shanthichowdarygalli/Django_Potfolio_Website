from django.urls import path, include
from . import views
urlpatterns = [

    #path('hi/',views.hi),
    path('employeelist/',views.employeelist, name = 'employeelist'),
    path('employeecreate/',views.employeecreate, name = 'employeecreate'),
    path('employeedetails/<pk>/',views.employeedetails, name = 'employeedetails'),
    path('employeeupdate/<pk>/', views.employeeupdate, name='employeeupdate'),
    path('employeedelete/<pk>/',views.employeedelete, name = 'employeedelete'),
]