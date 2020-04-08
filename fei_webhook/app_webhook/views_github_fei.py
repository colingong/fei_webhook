"""For github fei repo
   A Django demo
"""
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def fei_project(request):
    print(request.body)
    return HttpResponse('success')