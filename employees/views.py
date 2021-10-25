from django.shortcuts import render,redirect
from . models import Employee
# Create your views here.
def employeelist(request):
    employees = Employee.objects.all()
    employeeContext = {
        'employees': employees
    }
    return render(request,'employees/list_employees.html', context=employeeContext)

def employeecreate(request):
    if request.method == 'GET':
        # load create Employee Html Page
        return render(request,'employees/employee_registration_form.html')

    elif request.method == 'POST':
        # read the data from request
        # save the data into database
        eid = request.POST.get('eid')
        name = request.POST.get('name')
        age = request.POST.get('age')
        salary = request.POST.get('salary')
        address = request.POST.get('address')

        employee = Employee(eid=eid,name=name,age=age,salary=salary,address=address)
        employee.save()

        return redirect('/employees/employeelist/')


def employeedetails(request, pk):
    employee = Employee.objects.get(id=pk)

    empContext = {'employee': employee}
    return render(request, 'employees/employee_details.html', context=empContext)

def employeeupdate(request, pk):
    if request.method == 'GET':
        employee = Employee.objects.get(id=pk)
        empContext = {'employee': employee}
        return render(request, 'employees/employee_update_form.html', context=empContext)
    elif request.method == 'POST':
        id = request.POST.get('id')
        eid = request.POST.get('eid')
        name = request.POST.get('name')
        age = request.POST.get('age')
        salary = request.POST.get('salary')
        address = request.POST.get('address')

        employee = Employee.objects.get(id=id)
        employee.eid = eid
        employee.name = name
        employee.age = age
        employee.salary = salary
        employee.address = address

        employee.save()
        return redirect('/employees/employeelist/')

def employeedelete(request, pk):
    employee = Employee.objects.get(id=pk)
    employee.delete()
    return redirect('/employees/employeelist/')







