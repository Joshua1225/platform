import json
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


def test(request):
    return render(request,"test.html")

@csrf_exempt
def data(request):
    request.method
    print(request.POST)
    response={"backends":1}
    return HttpResponse(json.dumps(response))

def test(request):
    return render(request, 'test.html')