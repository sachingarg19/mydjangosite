# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


from django.http import HttpResponse
from django.http import request


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# Create your views here.
