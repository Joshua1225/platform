from django.forms import ModelForm
from django import forms
from backends.models import UnidentifiedAcademia,Papers
from haystack.forms import SearchForm

# 根据实际需求调整
class AcademiaForm(ModelForm):
    class Meta:
        model = UnidentifiedAcademia
        fields = "__all__"

# 上传文件表单
class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

#用于搜索的表单
class MySearchForm(SearchForm):
        start_year = forms.IntegerField(required=False)
        end_year = forms.IntegerField(required=False)
        author = forms.CharField(required=False)
        language = forms.CharField(required=False)

        def search(self):
            sqs = super(MySearchForm,self).search()

            if not self.is_valid():
                return self.no_query_found()

            if self.cleaned_data['start_year']:
                sqs = sqs.filter(year_gte=self.cleaned_data['start_year'])

            if self.cleaned_data['end_year']:
                sqs = sqs.filter(year_lte=self.cleaned_data['end_year'])

            if self.cleaned_data['language']:
                sqs = sqs.filter(lang=self.cleaned_data['language'])

            if self.cleaned_data['author']:
                sqs = sqs.filter(authors_contain=self.cleaned_data['author'])

                return sqs
