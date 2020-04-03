from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from share.util_file import log_event
import json

# Create your views here.

@csrf_exempt
def webhook(request):
    if request.method == 'POST':

        # 注意github配置时，选择的是form还是json

        # 如果是json
        data = json.loads(request.body)
        print(f'ref    :  {data.get("ref")}')
        print(f'before :  {data.get("before")}')
        print(f'after  :  {data.get("after")}')
        log_event(request.body.decode('utf-8'))

        # TODO: 如果是form
        
        return HttpResponse('ok')

    return HttpResponse('not post\n')