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
            ac = UnidentifiedAcademia.objects.get(username=request.session.get('username'))

            if len(ac) == 0:
                ans += [{'code': 3}]
                return JsonResponse(ans, safe=False)
            else:
                if obj.get('position') is not None:
                    ac.update(position=obj.get('position'))
                if obj.get('experience') is not None:
                    ac.update(experience=obj.get('experience'))
                if obj.get('education') is not None:
                    ac.update(education=obj.get('education'))
                if obj.get('tendency') is not None:
                    ac.update(tendency=obj('tendency'))

                ans += [{'code': 0}]
                return JsonResponse(ans, safe=False)
        else:
            ans += [{'code': 1}]
            return JsonResponse(ans, safe=False)
    else:
        ans += [{'code': 2}]
        return JsonResponse(ans, safe=False)