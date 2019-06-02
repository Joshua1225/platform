import json

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from backends.models import Papers,upload_paper_to

'''
upload_file() 上传文件

[{'code':0}]  上传成功
[{'code':1}]  拒绝使用GET方法
[{'code':2}]  论文不存在
'''
@csrf_exempt
# 上传文件
def upload_file(request):
    ans = []
    if request.method == 'POST':
        pid = request.POST.get('id')
        #sta 需要
        pfile = request.POST.get('file')
        paper = Papers.objects.filter(id=pid)
        if len(paper) == 0:
            ans += [{'code':2}]
            fpath = upload_paper_to(pid)
            print(fpath)

            return JsonResponse(ans, safe=False)
        else:
            fpath = upload_paper_to(pid)
            handle_uploaded_file(pfile,fpath)
            paper.update(pdf="具体存储的位置")
            ans += [{'code':0}]
            return JsonResponse(ans, safe=False)
    else:
        ans += [{'code':1}]
        return JsonResponse(ans, safe=False)

# 处理上传文件
def handle_uploaded_file(f,fpath):
    with open(fpath, 'wb+') as destination:     #需要修改为保存的位置
        for chunk in f.chunks():
            destination.write(chunk)
    destination.close()


# @csrf_exempt
# # 下载文件
# def download(request):
#     field = request.GET.get('field')
#     name = request.GET.get('name')
#     file = open( 'basedir'+field+'/'+name,'rb')    #basedir需要修改为文件保存根目录
#     response = FileResponse(file)
#     response['Content-Type']='application/msword'
#     response['Content-Disposition']='attachment;filename='+name
#     return response