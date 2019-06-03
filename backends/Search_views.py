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

    def build_page(self):
        """
        Paginates the results appropriately.

        In case someone does not want to use Django's built-in pagination, it
        should be a simple matter to override this method to do what they would
        like.
        """
        try:
            page_no = int(self.request.GET.get('page', 1))
        except (TypeError, ValueError):
            raise Http404("Not a valid number for page.")

        if page_no < 1:
            raise Http404("Pages should be 1 or greater.")

        start_offset = (page_no - 1) * self.results_per_page
        self.results[start_offset:start_offset + self.results_per_page]

        paginator = Paginator(self.results, self.results_per_page)

        try:
            page = paginator.page(page_no)
        except InvalidPage:
            raise Http404("No such page!")
        return (paginator, page)

    def create_response(self):
        """
        Generates the actual HttpResponse to send back to the user.
        """
        context = self.get_context()

        data = self.results.values("title", "author", "keywords", "year", "n_citation", "language")
        resp = json.dumps(list(data))
        return HttpResponse(resp)



