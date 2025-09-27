from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import Regristration

def registerView(request):
    next_url = request.GET.get("next", "/dashboard/")

    if request.method == "POST":
        form = Regristration(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data('password'))
            user.save()
            login(request, user)
            return redirect(next_url)
        
    else:
        form = Regristration()

    return render(request, "registration.html", {"form": form, "next": next_url})

def loginView(request):
    next_url = request.GET.get("next", "/dashboard/")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(next_url)
        
        else:
            return render(request, "login.html", {"error": "Invalid username or password", "next": next_url})

    return render(request, "login.html", {"next": next_url})

def logoutView(request):
    logout(request)
    return redirect("home")

