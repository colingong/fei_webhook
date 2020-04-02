from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from share.util_file import log_event

# Create your views here.
def alive(request):
    return HttpResponse('alive\n')

# dummy
@csrf_exempt
def webhook(request):
    if request.method == 'POST':
        log_event(request.body.decode('utf-8'))
        for k, _ in request.POST:
            print(f'key ---> {k}')
        print(request.POST.get('ref'))
        print(request.POST.get('before'))
        print(request.POST.get('after'))
        return HttpResponse('ok')

    return HttpResponse('not post\n')