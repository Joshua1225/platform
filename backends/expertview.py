import json

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from .forms import AcademiaForm, UploadFileForm
from backends.models import UnidentifiedAcademia
from backends.user import check_login

'''
editacademia() 修改专家信息

[{'code':0}]  修改成功
[{'code':1}]  拒绝使用GET方法
[{'code':2}]  用户未登录
[{'code':3}]  用户不存在
'''
@csrf_exempt
def editacademia(request):
    ans = []
    if check_login(request):
        if request.method == "POST":
            obj = json.loads(request.body)
            aid = obj["id"]
            #ans += [{"id": aid}]
            ac = UnidentifiedAcademia.objects.filter(id=aid)
            if len(ac) == 0:
                ans += [{'code': 3}]
                return JsonResponse(ans, safe=False)
            else:
                ac.update(position=obj["position"])
                ac.update(experience=obj["experience"])
                ac.update(education=obj["education"])
                ac.update(tendency=obj["tendency"])

                ans += [{'code': 0}]
                return JsonResponse(ans, safe=False)
        else:
            ans += [{'code': 1}]
            return JsonResponse(ans, safe=False)
    else:
        ans += [{'code': 2}]
        return JsonResponse(ans, safe=False)