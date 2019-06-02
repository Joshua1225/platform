
from backends.models import Papers
from haystack import indexes


class PapersIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
            return Papers

    def index_queryset(self, using=None):
        return self.get_model().objects.all()