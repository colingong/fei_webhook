from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from share.util_file import log_event
import json
import hashlib, hmac, base64
import os
from main_settings.settings import BASE_DIR
from .models import WebhookLog

# Create your views here.

FILENAME = 'github_webhook.log'
GITHUB_LOGFILE = os.path.join(BASE_DIR, 'log', FILENAME)

@csrf_exempt
def github_hook(request):
    if request.method == 'POST':
        # 注意github配置时，选择的是form还是json

        # 如果是json
        data = json.loads(request.body)
        repository = data.get("repository")
        head_commit = data.get("head_commit")

        """
        ref =
        before = 
        after = 

        # "repository":{"full_name": ...}
        repo_name = 

        # "repository":{"html_url": ...}
        html_url = 

        # "repository":{"hooks_url": ...}
        hooks_url = 

        # "head_commit": {"message": ...}
        commit_msg
        """
        github_log = WebhookLog()
        github_log.from_site = 'Github.com'
        github_log.ref = data.get("ref")
        github_log.before = data.get("before")
        github_log.after = data.get("after")
        github_log.repo_name = repository.get("full_name")
        github_log.html_url = repository.get("html_url")
        github_log.hooks_url = repository.get("hooks_url")
        github_log.commit_message = head_commit.get("message")
        github_log.save()
        # print(f'ref: {data.get("ref")} *** before: {data.get("before")} *** after: {data.get("after")}')

        print(request.headers.get('X-Hub-Signature'))
        raw = request.body
        key = '123456'.encode('utf-8')
        hashed = hmac.new(key, raw, hashlib.sha1)
        sign = hashed.hexdigest()
        print(f'check sign: {sign}')

        log_event(request.body.decode('utf-8'), GITHUB_LOGFILE)

        # TODO: 如果是form
        
        return HttpResponse('ok')

    return HttpResponse('not post\n')

def list_githublog(request, count=5):
    if request.method == 'GET':
        logs = WebhookLog.objects.all().order_by('-id')[:count]
        return render(request, 'app_webhook/github_log.html', {'logs': logs})

    return HttpResponse("no ok")
    