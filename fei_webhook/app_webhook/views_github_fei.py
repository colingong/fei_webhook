"""For github fei repo
   A Django demo
"""
from django.shortcuts import HttpResponse

def fei_project(request):
    print(request.body)
    return HttpResponse('success')