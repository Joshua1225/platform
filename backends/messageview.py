import json
import os

from django.http import HttpResponse, HttpResponseRedirect, FileResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from backends.user import check_login
from backends.models import Messages

'''
appeal(type, content,user_id,file,object_id)  用户提交申诉
http://154.8.237.76:8000/platform/appeal/
POST

[{"code":0}]  申诉成功
[{"code":1}]  拒绝使用GET方法
[{"code":2}]  用户未登录
[{"code":3}]  提交信息不完整
'''
@csrf_exempt
def register(request):
    if check_login(request):
        if request.method == "POST":
            data = json.loads(request.body.decode('utf-8'))
            type = data['type']
            content = data['content']
            time = data['time']
            userid = data['user_id']
            file = data['file']
            objectid = data['object_id']
            if(not type or not content or not userid or not file or not objectid):
                ans = [{'code':3}]
                return JsonResponse(ans, safe=False)
            else:
                fpath = os.path.join('documentations', userid, time)    #目前将id和时间戳作为文件命名
                with open(fpath, 'wb+') as destination:  # 需要修改为保存的位置
                    for chunk in file.chunks():
                        destination.write(chunk)
                destination.close()
                Messages.objects.create(type=type,content=content,time=time,userid=userid,file=fpath,objectid=objectid)
                ans = [{'code': 0}]
                return JsonResponse(ans, safe=False)
        else:
            ans = [{'code': 1}]
            return JsonResponse(ans, safe=False)
    else:
        ans = [{'code': 2}]
        return JsonResponse(ans, safe=False)