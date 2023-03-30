from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from datetime import date, time, datetime


def Home(request):
    return render(request, 'pages/home.html')
