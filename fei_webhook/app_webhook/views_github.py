from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from share.util_file import log_event
import json
import hashlib, hmac

# Create your views here.
@csrf_exempt
def webhook(request):
    if request.method == 'POST':
        # 注意github配置时，选择的是form还是json

        # 如果是json
        data = json.loads(request.body)
        print(f'ref: {data.get("ref")} *** before: {data.get("before")} *** after: {data.get("after")}')
        print(request.headers.get('X-Hub-Signature'))

        # payload caculate
        # payload = request.body.decode('utf-8')
        # signature = hashlib.sha1(request.body).hexdigest()
        # sign = hmac.new('123456', request.body, hashlib.sha1)
        sign = hmac.new('123456'.encode('utf-8'), request.body, hashlib.sha1)
        print(f'check sign: {sign}')
        log_event(request.body.decode('utf-8'))

        # TODO: 如果是form
        
        return HttpResponse('ok')

    return HttpResponse('not post\n')