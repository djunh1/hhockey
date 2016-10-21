from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    return HttpResponse('Authenticated Successfully')
                else:
                    return HttpResponse('Disabled Account')
            else:
                return HttpResponse('Invalid Login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


def edit(request):
    return render(request, 'account/edit.html')


def logged_out(request):
    logout(request)
    return render(request, 'registration/logged_out.html')


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            profile = Profile.objects.create(user=new_user)
            #profile = Profile.objects.create(user=new_user)
            new_user = authenticate(username=user_form.cleaned_data['username'],
                                        password=user_form.cleaned_data['password'])
            login(request, new_user)
            return render(request, 'account/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html',
                  {'user_form': user_form})


@login_required
def editprofile(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                       data=request.POST,
                                       files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated')
        else:
            messages.error(request, 'There was a problem updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user)
    return render(request, 'account/editProfile.html', {'user_form': user_form, 'profile_form': profile_form})
