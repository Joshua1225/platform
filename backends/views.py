import json
from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from django.shortcuts import render
from .models import Papers, UnidentifiedAcademia
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from .forms import AcademiaForm, UploadFileForm
from backends.models import UnidentifiedAcademia


def test(request):
    Papers.data_import()
    return HttpResponse("ok")
    # return render(request, "test.html")

@csrf_exempt
def data(request):
    request.method
    print(request.POST)
    response={"backends":1}
    return HttpResponse(json.dumps(response))






