from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .models import *


# Create your views here.


def receipe(request):

    if request.method == "POST":

        receipe_name = request.POST.get("receipe_name")
        receipe_descrip = request.POST.get("receipe_descrip")
        receipe_img = request.FILES.get("receipe_img")

        print(receipe_name)
        print(receipe_descrip)
        print(receipe_img)

        Receipe.objects.create(
            receipe_name=receipe_name,
            receipe_descrip=receipe_descrip,
            receipe_img=receipe_img
        )

    queryset = Receipe.objects.all()

    context = {
        'recipe': queryset
    }

    return render(request, 'receipe.html', context)


def delete_recipe(request, id):

    queryset = Receipe.objects.get(id=id)
    queryset.delete()

    return redirect('/receipe/')


def update_recipe(request, id):

    queryset = Receipe.objects.get(id=id)

    if request.method == "POST":

        receipe_name = request.POST.get("receipe_name")
        receipe_descrip = request.POST.get("receipe_descrip")
        receipe_img = request.FILES.get("receipe_img")

        queryset.receipe_name = receipe_name
        queryset.receipe_descrip = receipe_descrip

        if receipe_img:
            queryset.receipe_img = receipe_img

        queryset.save()

        return redirect('/receipe/')

    context = {
        'recipe': queryset
    }

    return render(request, 'update_recipe.html', context)


def login_page(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)

        if not user.exists():

            messages.error(
                request,
                "User is not registered! Please sign up."
            )

            return redirect('/login/')

        user_auth = authenticate(
            username=username,
            password=password
        )

        if user_auth is None:

            messages.error(
                request,
                "Invalid password or username."
            )

            return redirect('/login/')

        else:

            login(request, user_auth)

            return redirect('/receipe/')

    return render(request, 'login.html')


def logout_page(request):

    logout(request)

    return redirect('/login/')


def register(request):

    if request.method == 'POST':

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        print(first_name)
        print(last_name)
        print(username)
        print(email)
        print(password)

        # Check if username already exists
        if User.objects.filter(username=username).exists():

            messages.error(
                request,
                "User already exists!"
            )

            return redirect('/register/')

        # Create user
        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username
        )

        print(user)

        # Set password
        user.set_password(password)
        user.save()

        messages.success(
            request,
            "Account registered successfully!"
        )

        return redirect('/register/')

    return render(request, 'register.html')
