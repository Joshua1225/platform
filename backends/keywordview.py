import json
from django.http import HttpResponse, HttpResponseRedirect, FileResponse, JsonResponse
from django.shortcuts import render
import  random
keyword_value = [{"a": 0},{"a": 1},{"a": 2},{"a": 3},{"a": 4},{"a": 5},{"a": 6}
                 ]
def getkeyword(request):
    i = random.randint(0,3)
    keywordlist = []
    for j in range(2):
        keywordlist.append(keyword_value[i*2+j])

    return JsonResponse(keywordlist,safe=False)
