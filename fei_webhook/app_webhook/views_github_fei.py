"""For github fei repo
   A Django demo
"""
# import pathlib
from main_settings.settings import BASE_DIR
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .hook import GithubHookFeiProject
from share.env_conf import WebhookConfig

@csrf_exempt
def fei_project(request):
    if request.method == 'POST':
        # 注意github配置时，选择的是form还是json

        # 如果是json
        log = GithubHookFeiProject(request, sec_code=str(WebhookConfig.github_sec_code_fei))
        
        log.shell_script = WebhookConfig.github_hook_script_fei
        print(f'script file ---> {log.shell_script}')

        log.save_log()
        print(f'verified ---> {log.verified}')
        print('===> 0409')
        # dummy commit
        
        # TODO: 如果是form
        
        return HttpResponse('ok')

    return HttpResponse('not post\n')