
import json
import os

from django.http import HttpResponse, HttpResponseRedirect, FileResponse, JsonResponse
from django.shortcuts import render
from datetime import datetime
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from backends.user import check_login
from backends.models import Messages,Users
from backends.paperview import  handle_uploaded_file
'''
appeal(type, content,username,file,object_id)  用户提交申诉,需要用表单上传数据
http://154.8.237.76:8000/platform/appeal/
POST

[{"code":0}]  申诉成功
[{"code":1}]  拒绝使用GET方法
[{"code":2}]  用户未登录
[{"code":3}]  提交信息不完整
[{"code":4}]  该用户不存在或者不是专家 
'''
@csrf_exempt
def appeal(request):
    if check_login(request):
        if request.method == "POST":
            #data = json.loads(request.body.decode('utf-8'))
            type = request.POST.get('type')
            content =  request.POST.get('content')
            time = datetime.now()
            username =  request.POST.get('username')
            file =  request.POST.get('file')
            objectid =  request.POST.get('objectid')

            if type == '1' or type == '3':           #上传论文/论文申诉，需要身份为专家
                u = Users.objects.filter(username = username)
                if u and u.type == 1:
                    if(not type or not content or not username or not file or not objectid):
                        ans = [{'code': 3}]
                        return JsonResponse(ans, safe=False)
                    else:
                        if type == '1':
                            fpath = os.path.join('documentations','上传论文',username )    #目前将id和申诉类型作为路径
                        else:
                            fpath = os.path.join('documentations', '论文申诉', username)
                        handle_uploaded_file(file,fpath)
                        Messages.objects.create(type=type,content=content,time=time,userid=username,file=fpath,objectid=objectid)
                        ans = [{'code': 0}]
                        return JsonResponse(ans, safe=False)
                else:
                    ans = [{'code': 4}]

                    return JsonResponse(ans, safe=False)
            if type == '2':                                  #身份认证
                if (not type or not content or not username or not file or not objectid):
                    ans = [{'code': 3}]
                    return JsonResponse(ans, safe=False)
                else:
                    fpath = os.path.join('documentations', '身份认证', username)
                    handle_uploaded_file(file, fpath)
                    Messages.objects.create(type=type, content=content, time=time, userid=username, file=fpath,
                                            objectid=objectid)
                    ans = [{'code': 0}]
                    return JsonResponse(ans, safe=False)
            else:
                ans = [{'code': 3}]

                return JsonResponse(ans, safe=False)
        else:
            ans = [{'code': 1}]
            return JsonResponse(ans, safe=False)
    else:
        ans = [{'code': 2}]
        return JsonResponse(ans, safe=False)

