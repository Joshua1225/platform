from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.sessions.models import Session

import json

# Create your views here.

from .models import Users, UnidentifiedAcademia, Papers

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
        # data = request.POST
        print(data)
        u = Users.objects.get(username=data['username'])
        if (u):
            if (u.password == data['password']):
                '''在当前session容器中加入此次登录者的信息'''
                request.session['username'] = u.username
                if not request.session.session_key:
                    request.session.create()
                '''处理单点登录'''
                session_key = request.session.session_key
                session_data = Session.objects.get(session_key=session_key).session_data
                temp_session = Session.objects.filter(session_data=session_data).exclude(session_key=session_key)
                if temp_session:
                    temp_session.delete()
                # if same_session:
                #     for s in same_session:
                #         s.clear()
                '''返回登录成功'''
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
    request.session.flush()
    ans = [{
        "code": 0
    }]
    return JsonResponse(ans, safe=False)

'''
register(username, email, password, name)
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
        username = data['username']
        email = data['email']
        password = data['password']
        name = data['name']
        if (not username or not email or not password or not name):
            ans = [{
                'code': 3
            }]
            return JsonResponse(ans, safe=False)
        else:
            u = Users.objects.filter(username=username)
            if (u.exists()):
                ans = [{
                    'code': 2
                }]
            else:
                Users.objects.create(username=username, email=email, password=password, name=name)
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
        # u = Users.objects.filter(username=request.session.get("username")).first().values()
        u += [{
            "username": request.session.get("username")
        }]
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
    print(request.session.session_key)
    if request.method == "POST":
        if check_login(request):
            data = json.loads(request.body.decode("utf-8"))
            user = Users.objects.get(username=request.session.get('username', None))
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


"""
[{"code":0}]  关注/取关成功
[{"code":1}]  拒绝使用GET方法
[{"code":2}]  用户未登录
[{"code":3}]  专家不存在
[{"code":4}]  参数有误
"""
@csrf_exempt
def follow(request):
    ans = []
    data = json.loads(request.body)
    if request.method == "POST":
        if check_login(request):
            cur_user = Users.objects.filter(username=request.session['username'])
            academia = UnidentifiedAcademia.objects.filter(id=data.get('id'))
            if not academia:
                if not data.get('type'):
                    if data.get('type') == 0:
                        cur_user.follow.add(academia)
                    else:
                        cur_user.follow.remove(academia)
                    ans += [{
                       "code": 0
                    }]
                else:
                    ans += [{
                        "code": 4
                    }]
            else:
                ans += [{
                    "code": 3
                }]
        else:
            ans += [{
                "code": 2
            }]
    else:
        ans += [{
            "code": 1
        }]
    return JsonResponse(ans, safe=False)



"""
需要id type    type = 0 表示收藏 其他表示取消收藏
[{"code":0}]  收藏成功
[{"code":1}]  拒绝使用GET方法
[{"code":2}]  用户未登录
[{"code":3}]  论文不存在
[{"code":4}]  参数有误
"""
@csrf_exempt
def collect(request):
    ans = []
    data = request.POST
    # data = json.loads(request.body)
    if request.method == "POST":
        if check_login(request):
            cur_user = Users.objects.filter(username=data['username'])
            # cur_user = Users.objects.filter(username=request.Username)
            paper = Papers.objects.filter(id=data.get('id'))
            if not paper:
                if not data.get('type'):
                    if data.get('type') == 0:
                        cur_user.follow.add(paper)
                    else:
                        cur_user.follow.remove(paper)
                    ans += [{
                       "code": 0
                    }]
                else:
                    ans += [{
                        "code": 4
                    }]
            else:
                ans += [{
                    "code": 3
                }]
        else:
            ans += [{
                "code": 2
            }]
    else:
        ans += [{
            "code": 1
        }]
    return JsonResponse(ans, safe=False)

