from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Place, Comment

def home(request):
    places = Place.objects.all()[:5]
    return render(request, 'home.html', {'places': places})
    

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {"form": UserCreationForm})
    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'signup.html', {"form": UserCreationForm, "error": "Username already exists."})

        return render(request, 'signup.html', {"form": UserCreationForm, "error": "Passwords did not match."})

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {"form": AuthenticationForm, "error": "Username or password is incorrect."})

        login(request, user)
        return redirect('home')
    

@login_required
def signout(request):
    logout(request)
    return redirect('home')

def listPlaces(request):
    places = Place.objects.all()
    return render(request, 'listPlaces.html', {'places': places})


def placeDetails(request, placeId):
    
    place = get_object_or_404(Place, pk=placeId)
    comments = Comment.objects.filter(place=place)
    
    context = {
        'place': place,
        'comments': comments,
    }
    
    return render(request, 'placeDetails.html', context)
