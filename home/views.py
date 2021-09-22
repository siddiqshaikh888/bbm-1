from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Contact
from django.contrib.auth import authenticate, login, logout  
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Newsletter
from blogapp.models import BlogModel
from django.conf import settings
import requests
import json
# Create your views here.
def index(request):
    return render(request, 'index.html')
    #return HttpResponse("This is Home Page")
def sell(request):
    return render(request, 'core/sellwebsite1.html')

def how_to_sell(request):
    return render(request, 'core/how_to_sell.html')

def about(request):
    return render(request, 'core/about.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
     if request.method == "POST":
          name = request.POST.get('name')
          email = request.POST.get('email')
          subject = request.POST.get('subject')
          contact = Contact(name=name, email=email, subject=subject, date= datetime.today())
          contact.save()
          messages.success(request, 'Your message has been sent!')
     return render(request, 'contact.html')

def handleSignup(request):
    if request.user.is_authenticated:
        return redirect('home')
    elif request.method == 'POST':
            username = request.POST['username']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            #Check for Random warnings
            #Username should be 10 characters
            if len(username) > 50:
                messages.warning(request,"Username must be under 50 characters")
                return render(request, 'core/signup.html')

            #Username should be alphanumeric
            if not username.isalnum():
                messages.warning(request,"Username should only contain Letters and numbers")
                return render(request, 'core/signup.html')

            #Passwords should be same
            if password1 != password2:
                messages.warning(request,"Passwords do not Match")
                return render(request, 'core/signup.html')
            
            
            #Check if email exists
            if User.objects.filter(email=email).exists():
                messages.warning(request,"Email Already Exist")
                return render(request, 'core/signup.html')
            else:
                #Creating User
                myuser = User.objects.create_user(username, email, password1)
                myuser.first_name = first_name
                myuser.last_name = last_name
                myuser.save()
                messages.success(request,"Your Account has been Successfully Created")
                return redirect('home')

    else:
        #return render(request, 'signup.html')
        return redirect('core/dashboard')
def edit_user(request, user_id):

    user = User.objects.get(id=user_id)

def handleLogin(request):
    if request.user.is_authenticated:
        return redirect('home')
    elif request.method == 'POST':
            loginusername = request.POST['loginusername']
            loginpass = request.POST['loginpass']

            user = authenticate(username=loginusername, password=loginpass)
            

            if user is not None:
                login(request, user)
                messages.success(request, "Logged in Successfully")
                #return render(request, 'sell.html')
                return redirect('home')
            else:
                messages.warning(request, "Invalid Credentials, Please Try again")
                #return redirect('home')

    return render(request, 'login.html')
        #return HttpResponse('404 Not Found')
def handleLogout(request):
    logout(request)
    messages.info(request, "You are Logged Out")
    return render(request, 'login.html')

    #return render(request, 'newsletter.html')
    #return HttpResponse('handleLogout')

def search(request):
    searched = request.POST['searched']
    blogs = BlogModel.objects.filter(blog_title__contains=searched)
    if request.method == "POST":
        return render(request,'blogapp/search.html',{'searched':searched,'blogs':blogs})
    else:
        return render(request,'blogapp/search.html',{})
        
    #allPosts = BlogModel.objects.all()
    #params = {'allPosts': allPosts}

"""def sell(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            propurl = request.POST.get('propurl')
            desc = request.POST.get('desc')
            date = request.POST.get('date')
            monetized = request.POST.getlist('checks[]')
            sell = Sell(propurl=propurl, desc=desc, date = date, monetized = monetized )
            #response.user.Users_set.create(name=n)
            sell.save()
            messages.success(request, 'Your Message has been sent.')
        return render(request, 'sell.html')
    else:
        messages.info(request, 'Please Login first.')
    return redirect('/login')
    #return redirect('home')"""

def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html')
        if form.is_valid():
            user = form.save()

            account_type = request.POST.get('account_type', 'buyer')
            is_agree = request.POST.get('is_agree', 'checked')

            if account_type == 'seller':
                userprofile = Userprofile.objects.create(user=user, is_seller=True)
                userprofile.save()
            else:
                userprofile = Userprofile.objects.create(user=user)
                userprofile.save()
    
    else:
        messages.warning(request, 'Please Login first.')
        return redirect('/login')