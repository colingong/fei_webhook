"""接受从hhxx.me发出的webhook
"""
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, HttpResponse
import json
from share.env_conf import WebhookConfig
from .hook import HhxxGitHook

@csrf_exempt
def hhxx_hook(request):
    if request.method == 'GET':
        print(f'GET: request.path ===>{request.path}')
        for k, v in request.GET.items():
            print(f'{k} ---> {v}')
    elif request.method == 'POST':
        log = HhxxGitHook(request, sec_code=WebhookConfig.hhxx_sec_code)
        log.shell_script = WebhookConfig.hhxx_hook_script
        log.save_log()
        return HttpResponse('ok')

    return HttpResponse('nonono')