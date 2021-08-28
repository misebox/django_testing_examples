from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render

from packages.usecases import PackageUsecase


def index(request):
    return HttpResponse("Hello, world. You're at the packages index.")


def get_combo_page(request: HttpRequest):
    context = PackageUsecase.get_combo_page_context()
    return render(request, "packages/combo_page.html", context.dict())
