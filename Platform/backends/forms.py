from django.forms import ModelForm
from django import  forms
from .models import Users

# 根据实际需求调整
class UserForm(ModelForm):
    class Meta:
        model = Users

# 上传文件表单
class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()