from django.shortcuts import render
from decorator import api_view
from django.http import JsonResponse

@api_view(('GET'))
def get_data(request):
    person = {"nama" : 'nasrul'}
    return JsonResponse(person)
