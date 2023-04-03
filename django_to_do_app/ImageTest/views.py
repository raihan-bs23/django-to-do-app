from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from datetime import date, time, datetime
from .models import ImageShow
from django.shortcuts import get_object_or_404


def GetImage(request):
    getimages = ImageShow.objects.all()
    print("------------", getimages)
    return render(request, 'pages/view_image.html', {'getimage': getimages})
