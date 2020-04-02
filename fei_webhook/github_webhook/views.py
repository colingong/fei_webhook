from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def alive(request):
    return HttpResponse('alive\n')


@csrf_exempt
def webhook(request):
    if request.method == 'POST':
        print('got a post')
        print(request.body)
        return HttpResponse('ok')

    return HttpResponse('not post\n')