from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreation
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import CustomeUser
from .forms import CaptchaForm
# Create your views here.

def signup(request):
     if request.user.is_authenticated:
         return redirect('/')
     elif request.method == 'GET':
         form = CustomUserCreation()
         return render(request,'registration/signup.html', context={'form': form})
     else:
             form = CustomUserCreation(request.POST,request.FILES)
             if form.is_valid():
                 form.save()
                 email = request.POST.get('email')
                 password = request.POST.get('password1')
                 user = authenticate(email=email, password=password)
                 login(request,user)
                 return redirect('/accounts/signup/edit-profile/%i'%request.user.id)

             else:
                 messages.add_message(request, messages.ERROR, 'Invalid email or password')
                 return redirect(request.path_info)
        

        

def Login(request):
     if request.user.is_authenticated:
         return redirect('/')
     elif request.method == 'GET':
         form = AuthenticationForm()
         return render(request,'registration/login.html', context={'form': form})
     elif request.method == 'POST':
             email = request.POST.get('email')
             password = request.POST.get('password')      
             user = authenticate(email=email, password=password)
             if user is not None:
                 login(request,user)
                 return redirect('/')
             else:
                 messages.add_message(request, messages.ERROR, 'Invalid email or password')
                 return redirect(request.path_info)

@login_required
def Logout(request):
    logout(request)
    return redirect('/')

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib import messages

def change_password(request):
    if request.method == 'POST':
        # Create a PasswordChangeForm instance with the current user and the POST data
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            # Save the new password and update the user's session to prevent automatic logout
            user = form.save()
            update_session_auth_hash(request, user)
            # Display a success message and redirect to a success page
            messages.success(request, 'Your password has been successfully changed.')
            return render(request, 'registration/password_change_done.html', {'form': form})
        else:
            # Display error messages if the form is not valid
            messages.error(request, 'Please correct the form errors.')
    else:
        # Create a PasswordChangeForm instance for GET requests
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/password_change_form.html', {'form': form})