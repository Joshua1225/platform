from django.forms import ModelForm
from django import  forms
from .models import Unidentified_Academia

# 根据实际需求调整
class AcademiaForm(ModelForm):
    class Meta:
        model = Unidentified_Academia
        fields = "__all__"

# 上传文件表单
class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()