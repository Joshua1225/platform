import json
from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from .forms import AcademiaForm, UploadFileForm
from backends.models import UnidentifiedAcademia


def test(request):
    return render(request,"test.html")

@csrf_exempt
def data(request):
    request.method
    print(request.POST)
    response={"backends":1}
    return HttpResponse(json.dumps(response))


# 处理上传文件
def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:     #需要修改为保存的位置
        for chunk in f.chunks():
            destination.write(chunk)


@csrf_exempt
# 上传文件
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')       #修改为上传成功后的跳转页面
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


@csrf_exempt
# 下载文件
def download(request):
    field = request.GET.get('field')
    name = request.GET.get('name')
    file = open( 'basedir'+field+'/'+name,'rb')    #basedir需要修改为文件保存根目录
    response = FileResponse(file)
    response['Content-Type']='application/msword'
    response['Content-Disposition']='attachment;filename='+name
    return response


#修改专家信息
@csrf_exempt
def academia_edit(request):
    '''
        先把已有的用户信息读出来，然后判断用户请求是POST还是GET。如果是GET，则显示表单
        并将用户已有信息也显示在其中，如果是POST，则接收用户提交的表单信息，然后更新各个数据模型实例属性的值
    '''
    academia = UnidentifiedAcademia.objects.get(id = request.user.academia_id)  #这里是默认发送了user的信息
    if request.method == "POST":
        academia_form = AcademiaForm(request.POST)
        if academia_form.is_valid():
            academia_cd = academia_form.cleaned_data
            academia.position = academia_cd['position']
            academia.experience = academia_cd['experience']
            academia.education = academia_cd['education']
            academia.tendency = academia_cd['tendency']
            academia.save()
        return HttpResponseRedirect('填写你要跳转的url')
    else:
        academia_form = AcademiaForm(instance=request.user)
        return render(request, "填写你要跳转的html", {"user_form":academia_form})
