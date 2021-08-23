from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import auth, User
from django.contrib.auth.decorators import login_required
from .decorators import *
from .models import *
from .forms import *
from django.db.models import Q
from .filters import *

#Create your views here.

def index(request):
    return render(request, 'index.html')

#@login_required(login_url='/Login')
def About(request):
    return render(request, 'About.html')


@login_required(login_url='/Login')
def Profile(request):
    prof = request.user.profile #active object of Profile Model.
    form = MyProfile(instance=prof)
    return render(request, 'Profile.html', {'form':form})

def UpdateProfile(request, id):
    user = PROFILE.objects.get(pk=id)
    if request.method == 'POST':
        form = MyProfile(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('/Profile')
    return render(request, 'Profile.html', {'form':form})


#@login_required(login_url='/Login')
def Team(request):
    team = DIRECTORS.objects.order_by('-pk')[:6]
    return render(request, 'Team.html', {'team':team})


#@login_required(login_url='/Login')
def Search(request):
    Title = request.GET['title']
    About = request.GET['about']
    Description = request.GET['description']
    if Title:
        MySearch = BLOG.objects.filter(Q(Title=Title)|Q(Title__istartswith=Title)|Q(Title__icontains=Title))
    elif About:
        MySearch = BLOG.objects.filter(ABOUT=About)
    elif Description:
        MySearch = BLOG.objects.filter(Q(Description=Description)|Q(Description__istartswith=Description)|Q(Description__icontains=Description))
    else:
        return redirect('/')

    return render(request, 'Search.html', {'MySearch':MySearch})


#@login_required(login_url='/Login')
def Blogs(request):
    blog = BLOG.objects.order_by('-pk')
    filtered = MyFilter(request.GET, queryset=blog)
    blog = filtered.qs
    return render(request, 'Blogs.html', {'blog':blog, 'filtered':filtered})


def BlogDetails(request, slug):
    Details = BLOG.objects.get(pk=slug)
    return render(request, 'Search.html', {'Details':Details})


#@login_required(login_url='/Login')
def Services(request):
    projects = PROJECT.objects.order_by('-pk')[:4]
    return render(request, 'Services.html', {'projects':projects})

#@login_required(login_url='/Login')    
def Contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Message Sent Successifully')
            return redirect('/Contact')
    return render(request, 'Contact.html')


#ACCOUNTS
@unauthenticated_user
def Register(request):
    if request.method == 'POST':
        Fname = request.POST['fname']
        Lname = request.POST['lname']
        Username = request.POST['username']
        Email = request.POST['email']
        Pass1 = request.POST['password1']
        Pass2 = request.POST['password2']

        if len(Pass1)>=8 and len(Pass1)<=16:
            if Pass1==Pass2:
                if User.objects.filter(username = Username).exists():
                    messages.error(request, 'Username taken.!! Try another.')
                    return redirect('/Register')
                elif User.objects.filter(email = Email).exists():
                    messages.error(request, 'Email taken.!! Try another.')
                    return redirect('/Register')
                else:
                    user = User.objects.create_user(first_name=Fname, last_name=Lname, username=Username, email=Email, password=Pass1)
                    user.save()
                    user = request.POST['username']
                    messages.success(request, user + ' created successifully.')
                    return redirect('/Login')
            else:
                messages.error(request, 'Password mismatch.')
                return redirect('/Register')
        else:
            messages.error(request, 'Password must be between 8-16 characters long!!')
            return redirect('/Register')
    return render(request, 'Register.html')


@unauthenticated_user
def Login(request):
    if request.method == 'POST':
        next = request.GET.get('next') #Go to the Intended page.
        Username = request.POST['username']
        Pass1 = request.POST['password1']
        user = auth.authenticate(username=Username, password=Pass1)
        if user is not None:
            auth.login(request, user)
            if next:
                return redirect(next)
            return redirect('/')
        else:
            messages.error(request, 'Invalid Credentials!')
            return redirect('/Login')
    return render(request, 'Login.html')

def Logout(request):
    auth.logout(request)
    return redirect('/')

