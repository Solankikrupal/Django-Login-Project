from django.shortcuts import render
from LoginApp.forms import UserForm,UserProfileInfoForm

#this library for user_login so use it when you want to login
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout


# Create your views here.11
def index(call):
    return render(call,'home_page/index.html')

def registration(call):
    return render(call,'home_page/registration.html')

"""def login(call):
    return render(call,'home_page/login.html')
"""
@login_required
def special(call):
    return HttpResponse('Hey u logged in')

@login_required
def user_logout(call):
    logout(call)
    return HttpResponseRedirect(reverse('index'))



def register(call):

    registered = False #beacuse in registration.hyml we make condition if registered than thanks else form so we have to give False here

    if call.method == 'POST':

        user_form = UserForm(data = call.POST) #this line will refer to the forms.py

        profile_form = UserProfileInfoForm(data = call.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save() # this line will refer to model.py
            user.set_password(user.password)
            user.save()
            #end of user_form set_password beacuse we have add password in forms.py in additional fields

            profile = profile_form.save(commit = False) #false because it will overlapped upper form so for that we use onetoone fields to use that next line

            profile.user = user

            if 'profile_pic' in call.FILES:
                profile.profile_pic = call.FILES['profile_pic']

            profile.save()
            registered = True

        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(call,'home_page/registration.html',{
                            'user_form':user_form,
                            'profile_form':profile_form,
                            'registered':registered,
                        })


def user_login(call):

    if call.method == 'POST':
        username = call.POST.get('username') # get name from html file from login.html
        password = call.POST.get('password')

        user = authenticate(username = username,password = password) # this authenticate with databases

        if user:
            if user.is_active:
                login(call,user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse('Account is not active')

        else:
            print('someone tried to login but failed')
            print('UserName:{} and password:{}'.format(username,password))
            return HttpResponse('Invalid Credits')

    else:
        return render(call,'home_page/login.html',{})
