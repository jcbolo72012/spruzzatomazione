from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hi Ruby Hi Hi Hi Hi i made it work yippee!")