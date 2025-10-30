from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello, world. You're at the work05 index.")


def list(request):
    return HttpResponse("Hello, world. You're at the work05 list.")


def html(request):
    context = {"name": "haruki"}  # ← views.pyからテンプレートに渡す
    return render(request, "work05/index.html", context)
