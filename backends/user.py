from django.http import JsonResponse
from django.core import serializers

import json

# Create your views here.

from .models import Users

def check_login(request):
    flag = request.session.get("username", '')
    if not flag:
        return False
    else:
        return True

'''
login(username, password)

[{'code':0}]  登录成功
[{'code':1}]  拒绝使用GET方法
[{'code':2}]  账号不存在
[{'code':3}]  密码不对
'''
def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        u = Users.objects.filter(email=username)
        ans = []
        if (u):
            if (u[0].password == password):
                ans += [{
                        'code': 0
                    }]
                request.session['username'] = username
                return JsonResponse(ans, safe=False)
            else:
                ans += [{
                        'code': 3
                    }]
                return JsonResponse(ans, safe=False)
        else:
            ans += [{
                    'code': 2
                }]
            print(ans)
            return JsonResponse(ans, safe=False)
    else:
        ans = []
        ans += [{
                'code': 1
            }]
        return JsonResponse(ans, safe=False)

'''
logout()

[{'code':1}]  未登录
[{'code':0}]  注销成功
'''
def logout(request):
    ans = []
    if (check_login(request)):
        del request.session['username']
        ans += [{
                'code': 0
            }]
        return JsonResponse(ans, safe=False)
    else:
        ans += [{
                'code': 1
            }]
        return JsonResponse(ans, safe=False)

'''
register()

[{'code':0}]  注册成功
[{'code':1}]  拒绝使用GET方法
[{'code':2}]  用户已存在
'''
def register(request):
    ans = []
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        name = request.POST.get("name")
        if (len(email)==0 or len(password)==0 or len(name)==0):
            ans += [{
                'code': 2
            }]
            return JsonResponse(ans, safe=False)
        else:
            u = Users.objects.filter(email)
            if (len(u)==0):
                Users.objects.create(email=email, password=password, name=name)
                ans += [{
                    'code': 0
                }]
            else:
                ans += [{
                    'code': 2
                }]
            return JsonResponse(ans, safe=False)
    else:
        ans += [{
            'code': 1
        }]
        return JsonResponse(ans, safe=False)