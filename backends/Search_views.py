from haystack.views import SearchView
import json
from django.core.paginator import InvalidPage, Paginator
from django.http import HttpResponse
from django.shortcuts import render_to_response

class MySearchView(SearchView):
    def build_form(self, form_kwargs=None):
        data = None
        kwargs = {
            'load_all': self.load_all,
        }
        if form_kwargs:
            kwargs.update(form_kwargs)

        if len(self.request.body):
            data = json.loads(self.request.body)
            print(data)
            print(kwargs)
        if self.searchqueryset is not None:
            kwargs['searchqueryset'] = self.searchqueryset

        return self.form_class(data, **kwargs)

    def create_response(self):
        """
        Generates the actual HttpResponse to send back to the user.
        """
        data = json.loads(self.request.body)
        a = data['page_num']
        b = data['page_size']
        s = (a-1)*b
        data = self.results.values("title", "author", "keywords", "year", "n_citation", "language")[s:s+b]
        resp = json.dumps(list(data))
        return HttpResponse(resp)



