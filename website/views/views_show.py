from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from users.models import UserProfileInfo
from orders.models import Document, Order, Process
from orders.forms import DocumentForm, ProcessForm
from django.urls import reverse
from django.core.files.base import ContentFile
import io
import os
from google.cloud import vision
# from datetime import datetime


from PIL import Image, ImageFilter
import sys
from pyocr import pyocr
from pyocr import builders
import pytesseract


def show(request):
    show_check = False
    if request.method == 'GET':

        current_user = request.user
        document_list = Document.objects.filter(user = current_user).order_by('uploaded_at')
        image_names = []
        for doc in document_list:
            image_names.append(doc.document.name)
        image_num = len(image_names)
        if image_num > 0 :
            show_check = True
        else:
            return HttpResponse('No images to show')


    return render(request, 'relatedpages/show.html',
    {'show_check':show_check})
