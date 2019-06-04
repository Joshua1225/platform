from django.forms import ModelForm
from django import forms
from backends.models import UnidentifiedAcademia
from haystack.forms import SearchForm
from whoosh.analysis import StemmingAnalyzer
from haystack.query import SearchQuerySet

# 根据实际需求调整
class AcademiaForm(ModelForm):
    class Meta:
        model = UnidentifiedAcademia
        fields = "__all__"

# 上传文件表单
class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()


# 用于搜索的表单
class MySearchForm(SearchForm):
    q_not = forms.CharField(required=False, label="not_search", widget=forms.TextInput(attrs={'type': 'not_search'}))
    q_or = forms.CharField(required=False, label="not_search", widget=forms.TextInput(attrs={'type': 'not_search'}))
    author = forms.CharField(required=False)
    language = forms.CharField(required=False)
    start_year = forms.IntegerField(required=False)
    end_year = forms.IntegerField(required=False)
    order = forms.IntegerField(required=True)
    page_size = forms.IntegerField(required=True)
    page_num = forms.IntegerField(required=True)

    def search(self):
        if not self.is_valid():
            return self.no_query_found()
        if not self.cleaned_data.get('q'):
            return self.no_query_found()

        sqs = self.searchqueryset.auto_query(self.cleaned_data['q']).auto_query(self.cleaned_data['q_not'])
        str = self.cleaned_data['q_or']
        sqs_temp = SearchQuerySet()
        tokenana = StemmingAnalyzer()
        for token in tokenana(str):
            sqs_temp = sqs_temp.__or__(self.searchqueryset.auto_query(token.text))
        sqs = sqs.__and__(sqs_temp)
        if self.load_all:
            sqs = sqs.load_all()
        if self.cleaned_data['start_year']:
            sqs = sqs.filter(year__gte=self.cleaned_data['start_year'])
        if self.cleaned_data['end_year']:
            sqs = sqs.filter(year__lte=self.cleaned_data['end_year'])
        if self.cleaned_data['author']:
            str=self.cleaned_data['author']
            tokenana = StemmingAnalyzer()
            for token in tokenana(str):
                sqs = sqs.filter(author__icontains=token.text)
        if self.cleaned_data['language']:
            sqs = sqs.filter(language__content=self.cleaned_data['language'])
        if self.cleaned_data['order'] == 1:
            sqs = sqs.order_by('-year')
        if self.cleaned_data['order'] == 0:
            sqs = sqs.order_by('-n_citation')
        return sqs


