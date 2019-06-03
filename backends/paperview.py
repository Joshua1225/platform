import json,os

from django.http import JsonResponse, FileResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from backends.user import check_login
from backends.models import Papers,upload_paper_to

'''
upload_paper() 上传论文

[{'code':0}]  上传成功
[{'code':1}]  拒绝使用GET方法
[{'code':2}]  用户未登录
[{'code':3}]  论文不存在
'''
@csrf_exempt
# 上传文件
def upload_paper(request):
    ans = []
    if check_login(request):
        if request.method == 'POST':
            pid = request.POST.get('id')
        #sta 需要
            pfile = request.POST.get('file')
            paper = Papers.objects.filter(id=pid)
            if len(paper) == 0:       #论文不存在
                ans += [{'code': 3}]
                return JsonResponse(ans, safe=False)
            else:
                fpath = upload_paper_to(pid)
                handle_uploaded_file(pfile,fpath)
                paper.update(pdf=fpath)
                ans += [{'code':0}]
                return JsonResponse(ans, safe=False)
        else:
            ans += [{'code':1}]
            return JsonResponse(ans, safe=False)
    else:
        ans += [{'code': 2}]
        return JsonResponse(ans, safe=False)

# 处理上传论文文件
def handle_uploaded_file(f,fpath):
    with open(fpath, 'wb+') as destination:     #需要修改为保存的位置
        for chunk in f.chunks():
            destination.write(chunk)
    destination.close()


'''
download_paper() 下载论文
需要论文id 
return response: 正常下载
[{'code':1}]  论文不存在
[{'code':2}]  用户未登录
'''
@csrf_exempt
# 下载文件
def download_paper(request):
    ans = []
    if check_login(request):
        if request.method == 'POST':
            pid = request.POST.get('id')
            path = os.path.join('papers', pid)  #文件保存目录
            file = open(path,'rb')
            response = FileResponse(file)
            response['Content-Type'] = 'application/octet-stream'    #可以下载任意格式的文件
            response['Content-Disposition'] = 'attachment;filename=' + pid
            return response
        else:
            ans += [{'code': 1}]
            return JsonResponse(ans, safe=False)
    else:
        ans += [{'code': 2}]
        return JsonResponse(ans, safe=False)