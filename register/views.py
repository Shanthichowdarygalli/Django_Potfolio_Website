from django.shortcuts import render
from .models import Customer

# Create your views here.
def customer(request):

    if request.method == 'GET':
      return render(request,'register/customer.html')

    elif request.method == 'POST':
        # 1. read the submitted data

        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        availablecolours = request.POST.get('availablecolours')
        contactnumber = request.POST.get('contactnumber')
        emailid = request.POST.get('emailid')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        typeofcake = request.POST.get('typeofcake')

        #NameOfOccasion = request.POST.get('NameOfOccasion')

        birthday = request.POST.get('birthday')
        anniversary = request.POST.get('anniversary')
        kidsbirthday = request.POST.get('kidsbirthday')
        others = request.POST.get('others')

        NameOfOccasion = ''
        if birthday is not None:
            NameOfOccasion=NameOfOccasion+','+ birthday
        if anniversary is not None:
            NameOfOccasion = NameOfOccasion +','+  anniversary
        if kidsbirthday is not None:
            NameOfOccasion = NameOfOccasion+','+ kidsbirthday
        if others is not None:
            NameOfOccasion = NameOfOccasion+','+ others

        print('NameOfOccasion ==>',NameOfOccasion)

        byprice = request.POST.get('byprice')
        weight = request.POST.get('weight')

        #3. Insert the data into Database

        customer = Customer(firstname=firstname, lastname=lastname,
                          contactnumber=contactnumber, emailid=emailid, address=address, city=city,
                          state=state, NameOfOccasion=NameOfOccasion, weight=weight, byprice=byprice)
        customer.save()

        # 2.send received data to read_student_data.html
        customerData={
                    'firstname':firstname ,
                    'lastname': lastname,
                    'contactnumber': contactnumber,
                     'NameOfOccasion':NameOfOccasion,
                     'weight':weight,
                      'byprice':byprice,
                      'typeofcake':typeofcake,
                    #'availablecolours':availablecolours,


        }




        return render(request,'register/read_customerdata.html',context=customerData)











