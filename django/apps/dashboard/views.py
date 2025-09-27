from django.shortcuts import render, redirect

def landingPage(request):
    return render(request, 'dashboard/landing.html')