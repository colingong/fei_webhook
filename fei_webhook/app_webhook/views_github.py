from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from share.util_file import log_event
import json
import hashlib, hmac, base64
import os
from main_settings.settings import BASE_DIR
from .models import WebhookLog
from .shell_cmd import Cmds
from .hook import GithubHook
from main_settings.settings import BASE_DIR
import pathlib
from share.env_conf import WebhookConfig

# Create your views here.

FILENAME = 'github_webhook.log'
GITHUB_LOGFILE = os.path.join(BASE_DIR, 'log', FILENAME)

@csrf_exempt
def github_hook(request):
    if request.method == 'POST':
        # 注意github配置时，选择的是form还是json

        # 如果是json
        log = GithubHook(request, sec_code=str(WebhookConfig.github_sec_code))
        
        filename = 'demo_script.sh'
        dirname = pathlib.Path(BASE_DIR).parent
        # log.shell_script = os.path.join(dirname, filename)
        log.shell_script = WebhookConfig.github_hook_script
        print(f'script file ---> {log.shell_script}')

        log.save_log()
        print(f'verified ---> {log.verified}')
        
        # dummy commit
        
        # TODO: 如果是form
        
        return HttpResponse('ok')

    return HttpResponse('not post\n')

def list_githublog(request, count=5):
    if request.method == 'GET':
        logs = WebhookLog.objects.all().order_by('-id')[:count]
        return render(request, 'app_webhook/github_log.html', {'logs': logs})

    return HttpResponse("no ok")
