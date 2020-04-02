from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from share.util_file import log_event
import json

# Create your views here.
def alive(request):
    return HttpResponse('alive\n')

# dummy
@csrf_exempt
def webhook(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data.get('ref'))
        print(data.get('before'))
        print(data.get('after'))
        log_event(request.body.decode('utf-8'))
        return HttpResponse('ok')

    return HttpResponse('not post\n')