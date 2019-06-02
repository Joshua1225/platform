import json
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from .forms import AcademiaForm, UploadFileForm
from backends.models import UnidentifiedAcademia


'''
editacademia() 修改专家信息

[{'code':0}]  修改成功
[{'code':1}]  拒绝使用GET方法
[{'code':2}]  用户不存在
'''
@csrf_exempt
def editacademia(request):
    ans = []

    if request.method == "POST":
        id = request.POST.get("id")
        ac = UnidentifiedAcademia.objects.filter(id)
        if len(ac) == 0:
            ans += [{'code': 2}]
            return JsonResponse(ans, safe=False)
        else:
            ac.position = request.POST.get("position")
            ac.experience = request.POST.get("experience")
            ac.education = request.POST.get("education")
            ac.tendency = request.POST.get("tendency")
            ac.save()
            ans += [{'code': 0}]
            return JsonResponse(ans, safe=False)
    else:
        ans += [{'code': 1}]
        return JsonResponse(ans, safe=False)