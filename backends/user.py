from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.sessions.models import Session

import json

# Create your views here.

from .models import Users

def check_login(request):
    flag = request.session.get("username", None)
    if not flag:
        return False
    else:
        return True

'''
login(username, password)
http://154.8.237.76:8000/platform/login/
POST

[{"code":0}]  登录成功
[{"code":1}]  拒绝使用GET方法
[{"code":2}]  账号不存在
[{"code":3}]  密码不对
'''
@csrf_exempt
def login(request):
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        u = Users.objects.filter(email=data['username'])
        if (u):
            #if (u.password == data['password']):
            if (u.password == data['password']):
                request.session['username'] = u.email
                session_key = request.session.session_key
                session_data = Session.objects.filter(session_key=session_key).first().session_data
                Session.objects.filter(session_data=session_data).exclude(session_key=session_key).delete()
                ans = [{
                    'code': 0
                }]
                return JsonResponse(ans, safe=False)
            else:
                ans = [{
                        'code': 3
                    }]
                return JsonResponse(ans, safe=False)
        else:
            ans = [{
                    'code': 2
                }]
            return JsonResponse(ans, safe=False)
    else:
        ans = [{
                'code': 1
            }]
        return JsonResponse(ans, safe=False)

'''
logout(sessionid)
http://154.8.237.76:8000/platform/logout/
'''
@csrf_exempt
def logout(request):
    Session.objects.filter(session_key=request.session.session_key).delete()

'''
register(email, password, name)
http://154.8.237.76:8000/platform/register/
POST

[{"code":0}]  注册成功
[{"code":1}]  拒绝使用GET方法
[{"code":2}]  用户已存在
[{"code":3}]  信息有空
'''
@csrf_exempt
def register(request):
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        email = data['email']
        password = data['password']
        name = data['name']
        if (not email or not password or not name):
            ans = [{
                'code': 3
            }]
            return JsonResponse(ans, safe=False)
        else:
            u = Users.objects.filter(email=email)
            if (u.exists()):
                ans = [{
                    'code': 2
                }]
            else:
                Users.objects.create(email=email, password=password, name=name)
                ans = [{
                    'code': 0
                }]
            return JsonResponse(ans, safe=False)
    else:
        ans = [{
            'code': 1
        }]
        return JsonResponse(ans, safe=False)


@csrf_exempt
def userinfo(request):
    u = []
    if (check_login(request)):
        u = Users.objects.filter(email=request.session.get("username")).first().values()
    return JsonResponse(u, safe=False)

"""
[{"code":0}]  修改成功
[{"code":1}]  拒绝使用GET方法
[{"code":2}]  用户未登录
[{"code":3}]  信息不合法
[{"code":4}]  邮箱已被占用
[{"code":5}]  密码最少8位，最长21位
"""

@csrf_exempt
def change_info(request):
    ans = []
    if request.method == "POST":
        if check_login(request):
            data = json.loads(request.body)
            user = Users.objects.filter(username=request.session['username'])
            ans += [{
                'code': 0
            }]
            if data.get('password') is not None:
                if 8 <= len(data.get('password')) <= 21:
                    user.update(password=data.get('password'))
                else:
                    ans[0]['code'] = 5
            elif data.get('interest') is not None:
                user.update(interest=data.get('interest'))
            elif data.get('signature') is not None:
                user.update(signature=data.get('signature'))
            elif data.get('email') is not None and re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", data.get('email')):
                if not Users.objects.filter(email=data.get('email')):
                    ans[0]['code'] = 4
                else:
                    user.update(email=data.get('email'))
            else:
                ans[0]['code'] = 3
        else:
            ans += [{
                'code': 2
            }]
    else:
        ans += [{
            'code': 1
        }]
    return JsonResponse(ans, safe=False)

