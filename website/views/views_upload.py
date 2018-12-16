from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from users.models import UserProfileInfo
from orders.models import Document, Order
from orders.forms import DocumentForm
from django.urls import reverse
from django.core.files.base import ContentFile
import uuid
import io
import os
from google.cloud import vision
# from datetime import datetime



from PIL import Image, ImageFilter
import sys
from pyocr import pyocr
from pyocr import builders
import pytesseract


def model_form_upload(request):
    upload_check = False
    if request.method == 'POST':
        current_user = request.user
        order_list = Order.objects.filter(user=current_user, is_finished = False).order_by('-id')
        if len(order_list) > 0 :
            order = order_list[0]
        else:
            order = Order(user = current_user)
            order.save()
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid:
            document = form.save(commit=False)
            document.user = current_user
            document.order = order
            document.save()
            upload_check = True

        else:
            print(form.errors)
    else:
        form = DocumentForm()
    return render(request, 'relatedpages/upload.html', {
        'form': form
    })


def test(request):
    image = Image.open('/home/sina/work/ocr/ocr/website/media/uploaded/test.png')
    image.filter(ImageFilter.SHARPEN)
    txt = pytesseract.image_to_string(
    image,
    lang='eng')
    return HttpResponse(txt)
