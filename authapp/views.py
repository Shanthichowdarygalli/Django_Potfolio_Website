from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import ProfilePic
from django.urls import reverse

# Create your views here.
def user_registration(request):
    if request.method == 'GET':
        return render(request, 'authapp/user_registration.html')
    elif request.method == 'POST':
        # 1. Read input data
        username = request.POST.get('username') #*
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email') #*
        password = request.POST.get('password') #*
        cpassword = request.POST.get('cpassword') #*

        #2. Validate Mandaterary Fields
        if username == '' or email == '' or password == '' or cpassword == '':
            messages.error(request,'Mandatory fields are missing, Please check')
            return render(request, 'authapp/user_registration.html')

        #3. Validate password & confirm password, both should be equal
        if password != cpassword:
            messages.error(request, 'Password & Confirm Password both are not matching!!!')
            return render(request, 'authapp/user_registration.html')

        #4. Validate whether user name is alrady in use or not
        if User.objects.filter(username=username).exists():
            messages.error(request, 'User name already in use!!!')
            return render(request, 'authapp/user_registration.html')

        #5. Validate whether email id is alrady in use or not
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'User email id already in use!!!')
            return render(request, 'authapp/user_registration.html')
        else:
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
            messages.success(request, 'User Created Successfully!!!')
        return render(request, 'authapp/profile.html', context={'user': user})

def user_profile(request):
    return render(request,'authapp/profile.html')

def user_login(request):
    if request.method == 'GET':
        return render(request, 'authapp/login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)#User
        if user is not None:
            login(request, user)
            return render(request, 'authapp/profile.html')
        else:
            messages.error(request, 'User is not Valid, pls check!!!')
            return render(request, 'authapp/login.html')

def user_logout(request):
    logout(request)
    return redirect('/authapp/login/')

def add_profile_pic(request):
    form = ProfilePic()
    contextObj = {'form': form}

    if request.method == 'POST':
        #save profie pic in DB
        form = ProfilePic(request.POST, request.FILES) #ModelForm = Form + From Data(Model)
        if form.is_valid():
            user_objt = form.save(commit=False)
            user_objt.user = request.user
            user_objt.save()
            return HttpResponseRedirect(reverse('profile'))

    return render(request, 'authapp/profile_pic_add.html', context=contextObj)

def update_profile_pic(request):
    form = ProfilePic(instance=request.user.user_profile)
    contextObj = {'form': form}

    if request.method == 'POST':
        form = ProfilePic(request.POST, request.FILES, instance=request.user.user_profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('profile'))

    return render(request, 'authapp/profile_pic_add.html', context=contextObj)