import os

from django.contrib.sessions.backends.db import SessionStore
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.sessions.models import Session
from django.core import serializers

import json
import re
import random

# Create your views here.

from .models import Users, UnidentifiedAcademia, Papers


def check_login(request):
    request.session.clear_expired()
    flag = request.session.get("username", None)
    if not flag:
        return False
    else:
        return True

'''
login(username, password)
http://154.8.237.76:8000/login
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
        uu = Users.objects.filter(username=data['username'])
        if (uu.exists()):
            u = uu.first()
            if (u.password == data['password']):
                '''在当前session容器中加入此次登录者的信息'''
                request.session['username'] = u.username
                if not request.session.session_key:
                    request.session.create()
                '''处理单点登录'''
                session_key = request.session.session_key
                session_data = Session.objects.get(session_key=session_key).session_data
                temp_sessions = Session.objects.filter(session_data=session_data).exclude(session_key=session_key)
                if temp_sessions.exists():
                    for ts in temp_sessions:
                        SessionStore(ts.session_key).clear()
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
logout()
http://154.8.237.76:8000/logout/
'''
@csrf_exempt
def logout(request):
    request.session.clear()
    ans = [{
        "code": 0
    }]
    return JsonResponse(ans, safe=False)

'''
register(username, email, password, name)
http://154.8.237.76:8000/register
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
def uinfo(request):
    if request.method=="POST":
        data = json.loads(request.body.decode('utf-8'))
        ans=[]
        u = Users.objects.filter(username=data['username'])
        uinfo = serializers.serialize("json", u)
        if u.first().type == 1:
            a = UnidentifiedAcademia.objects.filter(id=u.first().academia_id)
            #ainfo = UnidentifiedAcademiaSerializer(a, many=True)
            ainfo = serializers.serialize("json", a)
            ans += [{
                "code": 0,
                "userinfo": json.loads(uinfo),
                "academy": 1,
                "academyinfo": json.loads(ainfo)
            }]
        else:
            ans += [{
                "code": 0,
                "userinfo": json.loads(uinfo),
                "academy": 0,
                "academyinfo": []
            }]
        return JsonResponse(ans, safe=False)
    else:
        ans = [{
            "code": 2,
            "userinfo": {}
        }]
        return JsonResponse(ans, safe=False)
'''
userinfo()
POST

返回的是一个JsonArray，内部一个JsonObject
'''
@csrf_exempt
def userinfo(request):
    if request.method=="POST":
        ans=[]
        if (check_login(request)):
            u = Users.objects.filter(username=request.session.get("username"))
            #uinfo = UsersSerializer(u, many=True)
            uinfo = serializers.serialize("json", u)
            if u.first().type == 1:
                a = UnidentifiedAcademia.objects.filter(id=u.first().academia_id)
                #ainfo = UnidentifiedAcademiaSerializer(a, many=True)
                ainfo = serializers.serialize("json", a)
                ans += [{
                    "code": 0,
                    "userinfo": json.loads(uinfo),
                    "academy": 1,
                    "academyinfo": json.loads(ainfo)
                }]
            else:
                ans += [{
                    "code": 0,
                    "userinfo": json.loads(uinfo),
                    "academy": 0,
                    "academyinfo": []
                }]
        else:
            ans += [{
                "code": 1,
                "userinfo": [],
                "academy": 0,
                "academyinfo": []
            }]
        return JsonResponse(ans, safe=False)
    else:
        ans = [{
            "code": 2,
            "userinfo": {}
        }]
        return JsonResponse(ans, safe=False)


"""
[{"code":0}]  修改成功
[{"code":1}]  拒绝使用GET方法
[{"code":2}]  用户未登录
[{"code":3}]  参数不合法
[{"code":4}]  邮箱已被占用
[{"code":5}]  密码最少8位，最长21位
"""
@csrf_exempt
def change_info(request):
    ans = []
    mark = False
    print(request.session.session_key)
    if request.method == "POST":
        if check_login(request):
            data = json.loads(request.body.decode("utf-8"))
            user = Users.objects.filter(username=request.session.get('username'))
            ans += [{
                'code': 0
            }]
            if data.get('password', None) is not None:
                mark = True
                if 8 <= len(data.get('password', None)) <= 21:
                    user.update(password=data.get('password'))
                else:
                    ans[0]['code'] = 5
            if data.get('interest', None) is not None:
                user.update(interest = data.get('interest'))
                mark = True
            if data.get('signature', None) is not None:
                user.update(signature=data.get('signature'))
                mark = True
            if data.get('email', None) is not None and re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", data.get('email')):
                mark = True
                if Users.objects.filter(email=data.get('email')):
                    ans[0]['code'] = 4
                else:
                    user.update(email=data.get('email'))
            if user.first().type == 1:
                academia = UnidentifiedAcademia.objects.filter(id=user.first().academia_id)
                if data.get('position', None) is not None:
                    academia.update(position=data.get('position'))
                    mark = True
                if data.get('education', None) is not None:
                    academia.update(education=data.get('education'))
                    mark = True
                if data.get('tendency', None) is not None:
                    academia.update(tendency=data.get('tendency'))
                    mark = True
                if data.get('experience', None) is not None:
                    academia.update(experience=data.get('experience'))
                    mark = True
            if not mark:
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
    data = json.loads(request.body.decode("utf-8"))
    if request.method == "POST":
        if check_login(request):
            cur_user = Users.objects.filter(username=data.get('username')).first()
            # cur_user = Users.objects.filter(username=request.session['username']).first()
            academia = UnidentifiedAcademia.objects.get(id=data.get('id'))
            if academia:
                if data.get('type') is not None:
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
    data = json.loads(request.body.decode("utf-8"))
    if request.method == "POST":
        if check_login(request):
            # cur_user = Users.objects.filter(username=request.session['username']).first()
            cur_user = Users.objects.filter(username=data.get('username')).first()
            paper = Papers.objects.get(id=data.get('id'))
            print(paper)
            if paper:
                if data.get('type') is not None:
                    if data.get('type') == 0:
                        cur_user.collect.add(paper)
                    else:
                        cur_user.collect.remove(paper)
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

'''
relatedacademia(paperid)

code:0  登录状态操作
code:1  未登录操作
code:2  非POST方法
'''
@csrf_exempt
def relatedacademia(request):
    ans = []
    relauth = []
    '''首先随机获取6个专家信息'''
    relauth += json.loads(serializers.serialize('json', UnidentifiedAcademia.objects.order_by('?')[:6]))

    if request.method == "POST":
        '''按照相应规则寻找正确的相关专家'''
        data = json.loads(request.body.decode('utf-8'))
        if check_login(request):
            '''获取前端给的论文id'''
            curpapers = Papers.objects.filter(id=data['paperid'])
            if curpapers.exists():
                '''找到该论文的第一作者'''
                curpaper = curpapers.first()
                curpaperauthor = json.loads(json.dumps(eval(curpaper.authors)))
                # curpaperauthor = curpaper.authors
                '''把这篇论文的所有作者的专家信息加载'''
                for cpa in curpaperauthor:
                    relauth += academiainfo(cpa['id'])
                curauthors = UnidentifiedAcademia.objects.filter(id=curpaperauthor[0]['id'])
                '''数据库中存在这个第一作者'''
                if curauthors.exists():
                    curauthor = curauthors.first()
                    '''找到这个作者的其他论文'''
                    pubs = json.loads(json.dumps(eval(curauthor.pubs)))
                    # pubs = curauthor.pubs
                    for p in pubs:
                        papers = Papers.objects.filter(id=p['i'])
                        '''第一作者的某篇论文在数据库中存在'''
                        if papers.exists():
                            paper = papers.first()
                            paperauthor = json.loads(json.dumps(eval(paper.authors)))
                            # paperauthor = paper.authors
                            for pa in paperauthor:
                                relauth += academiainfo(pa['id'])
                    ans = [{
                        'code': 0,
                        'relauth': relauth
                    }]
                else:
                    ans = [{
                        'code': 0,
                        'relauth': relauth
                    }]
            else:
                ans = [{
                    'code': 0,
                    'relauth': relauth
                }]
        else:
            ans = [{
                'code': 1,
                'relauth': relauth
            }]
    else:
        ans = [{
            'code': 2,
            'relauth': relauth
        }]
    return JsonResponse(ans, safe=False)

def academiainfo(aid):
    academias = UnidentifiedAcademia.objects.filter(id=aid)
    if academias.exists():
        academia = serializers.serialize("json", academias)
        return json.loads(academia)
    else:
        return []

'''
根据专家id获取专家信息
academyid(academyid)
'''
@csrf_exempt
def academyinfo(request):
    ans = []
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        if check_login(request):
            academias = UnidentifiedAcademia.objects.filter(id=data['academyid'])
            academia = serializers.serialize("json", academias)
            ans = [{
                'code': 0,
                'academyinfo': json.loads(academia)
            }]
        else:
            ans = [{
                'code':1,
                'academyinfo':[]
            }]
    else:
        ans = [{
            'code':2,
            'academyinfo':[]
        }]
    return JsonResponse(ans, safe=False)



'''
listcollection()
'''
@csrf_exempt
def listcollection(request):
    ans = []
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        if check_login(request):
            unow = Users.objects.filter(username=request.session['username'])
            # unow = Users.objects.filter(username=data['username']).first().collect.all()
            collected = serializers.serialize('json', unow)
            ans +=[{
                'code':0,
                'followed':json.loads(collected)
            }]
        else:
            ans += [{
                'code': 1,
                'followed': []
            }]
    else:
        ans += [{
            'code': 2,
            'followed': []
        }]
    return JsonResponse(ans, safe=False)


'''
listfollow()
'''
@csrf_exempt
def listfollow(request):
    ans = []
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        if check_login(request):
            unow = Users.objects.filter(username=request.session['username'])
            # unow = Users.objects.filter(username=data['username']).first().follow.all()
            followed = serializers.serialize('json', unow)
            ans +=[{
                'code':0,
                'followed':json.loads(followed)
            }]
        else:
            ans += [{
                'code': 1,
                'followed': []
            }]
    else:
        ans += [{
            'code': 2,
            'followed': []
        }]
    return JsonResponse(ans, safe=False)



@csrf_exempt
def recommend(request):
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        if check_login(request):
            paper_list = []
            user = Users.objects.get(username=request.session['username'])
            follow_list = user.follow.all()
            collect_list = user.collect.all()
            if follow_list.exists():
                for follow in follow_list:
                    papers_tmp = json.loads(json.dumps(eval(follow.pubs)))
                    for paper_tmp in papers_tmp:
                        tmp_paper_set = Papers.objects.filter(id=paper_tmp.get('i'))
                        if len(tmp_paper_set) > 0:
                            paper_list.append(tmp_paper_set.first())
            if collect_list.exists():
                for collect in collect_list:
                    paper_list.extend(get_related_paper(collect.id, 0))
            if len(paper_list) < 10:
                paper_list.extend(Papers.objects.filter('?')[0:10])
            paper_list_json = serializers.serialize("json", paper_list)
            ans = [{
                "code": 0,
                "paper": paper_list_json
            }]
            return JsonResponse(ans, safe=False)
        else:
            ans += [{
                "code": 2
            }]
            return JsonResponse(ans, safe=False)
    else:
        ans += [{
            "code": 1
        }]
        return JsonResponse(ans, safe=False)


@csrf_exempt
def relatedpaper(request):
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        if data.get('id', None):
            if Papers.objects.filter(id=data.get('id')).exists():
                paper_list = serializers.serialize("json", get_related_paper(data.get('id'), 10))
                ans = [{
                    "code": 0,
                    "paper": paper_list
                }]
                return JsonResponse(ans, safe=False)
            else:
                """搜索的论文不存在"""
                ans = [{
                    'code': 3
                }]
        else:
            """参数有误"""
            ans = [{
                "code": 2
            }]
    else:
        ans = [{
            "code": 1
        }]
    return JsonResponse(ans, safe=False)


def get_related_paper(paperid, least=0):
    related_paper_list = []
    keyword_list = json.loads(json.dumps(eval(Papers.objects.get(id=paperid).keywords)))
    if keyword_list is not None:
        for keyword in keyword_list:
            related_paper_list.extend(Papers.objects.filter(abstract__icontains=keyword))
    if len(related_paper_list) < least:
        related_paper_list.extend(Papers.objects.order_by('?')[:10])
    return related_paper_list





BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
'''
upload_avator() 上传头像

[{'code':0}]  上传成功
[{'code':1}]  拒绝使用GET方法
[{'code':2}]  用户未登录
'''
@csrf_exempt
# 上传文件
def upload_avator(request):
    ans = []

    if request.method == 'POST':
        if check_login(request):

            ufile = request.body
            uid = request.session['username']
            paper = Papers.objects.filter(id=uid)
            fpath = os.path.join(BASE_DIR, 'static','avators',uid)
            handle_uploaded_file(ufile,fpath)
            paper.update(pdf=fpath)
            ans += [{'code':0}]
            return JsonResponse(ans, safe=False)
        else:
            ans += [{'code':2}]
            return JsonResponse(ans, safe=False)
    else:
        ans += [{'code': 1}]
        return JsonResponse(ans, safe=False)

# 处理上传文件
def handle_uploaded_file(f,fpath):
    with open(fpath, 'wb+') as destination:     #需要修改为保存的位置
        destination.write(f)
    destination.close()