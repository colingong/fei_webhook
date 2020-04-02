from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from share.util_file import log_event

# Create your views here.
def alive(request):
    return HttpResponse('alive\n')


@csrf_exempt
def webhook(request):
    if request.method == 'POST':
        request_post_dict = request.POST.dict()
        log_event(request.body.decode('utf-8'))
        print(request_post_dict.get('before'))
        print(request_post_dict.get('after'))
        return HttpResponse('ok')

    return HttpResponse('not post\n')