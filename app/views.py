from django.shortcuts import render, redirect
from .forms import UserRegister, LoginForm
from . models import User
from django.db.models import Q
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib import messages


def home(request):
    return render(request, 'home.html')


def register_doc(request):
    if request.method == 'POST':
        form = UserRegister(request.POST, request.FILES)
        if form.is_valid():
            ref_id = form.cleaned_data['username']
            form.save()
            c = User.objects.get(Q(username=ref_id))
            print(c)
            c.is_doctor = True
            if(len(request.FILES) != 0):
                c.profile_pic = request.FILES['image']
            c.save()
            messages.success(
                request, 'You(Doctor) have registered successfully. Login In Now')
            return redirect('login')
        else:
            msg = 'Form is not valid'
            return render(request, 'register.html', {'form': form, 'msg': msg})
    else:
        form = UserRegister()
        return render(request, 'register.html', {'form': form})


def register_pat(request):
    if request.method == 'POST':
        form = UserRegister(request.POST, request.FILES)
        if form.is_valid():
            ref_id = form.cleaned_data['username']
            form.save()
            c = User.objects.get(Q(username=ref_id))
            print(c)
            c.is_patient = True
            if(len(request.FILES) != 0):
                c.profile_pic = request.FILES['image']
            c.save()
            messages.success(
                request, 'You(Patient) have registered successfully. Login In Now')
            return redirect('login')
        else:
            msg = 'Errors while validating the form. Try Again!'
            return render(request, 'registerpat.html', {'form': form, 'msg': msg})
    else:
        form = UserRegister()
        return render(request, 'registerpat.html', {'form': form})


def login(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_doctor is True:
                details = User.objects.filter(username=username)
                auth_login(request, user)
                print(details)
                return render(request, 'doctor.html', {'details': details})
            elif user is not None and user.is_doctor is False:
                details = User.objects.filter(username=username)
                auth_login(request, user)
                print(details)
                return render(request, 'patient.html', {'details': details})
            else:
                msg = 'You have entered incorrect username or password'
                return render(request, 'login.html', {'form': form, 'msg': msg})
        else:
            msg = 'Error has ocuured. Try Again'
    return render(request, 'login.html', {'form': form, 'msg': msg})
