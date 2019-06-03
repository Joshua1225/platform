
from backends.models import Papers
from haystack import indexes


class PapersIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    year = indexes.IntegerField(model_attr='year', null=True)
    language = indexes.CharField(model_attr='lang', null=True)
    author = indexes.CharField(model_attr='authors', null=True)
    title = indexes.CharField(model_attr='title', null=True)
    keywords = indexes.CharField(model_attr='keywords', null=True)
    n_citation = indexes.IntegerField(model_attr='n_citation', null=True)

    def get_model(self):
        return Papers

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
