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