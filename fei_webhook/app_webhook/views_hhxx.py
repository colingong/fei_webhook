"""接受从hhxx.me发出的webhook
"""
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, HttpResponse
import json
from share.env_conf import WebhookConfig

@csrf_exempt
def hhxx_hook(request):
    if request.method == 'GET':
        print(f'GET: request.path ===>{request.path}')
        for k, v in request.GET.items():
            print(f'{k} ---> {v}')
    elif request.method == 'POST':
        print(f'POST: request.path ===>{request.path}')
        data = json.loads(request.body)
        for k, v in data.items():
            print(f'{k} ---> {v}')
        if data.get('sec') == WebhookConfig.hhxx_sec_code:
            print('GOOD')
        else:
            print('wrong pass ===')
    
    return HttpResponse('no')