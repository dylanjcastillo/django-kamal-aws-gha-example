import csv
import json

from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render


def home(request: HttpRequest) -> HttpResponse:
    return render(request, "home.html")


def health(request: HttpRequest) -> JsonResponse:
    return JsonResponse({"status": "OK"})
