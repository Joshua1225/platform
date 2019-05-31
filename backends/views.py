from django.shortcuts import render,get_object_or_404
from django.template import loader
from .models import Question, Choice
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views import generic
from django.http import Http404

# Create your views here.


def advanced_search(request):
    if request.method == "POST":
        param = request.POST
