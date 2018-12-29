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
        order_list = Order.objects.filter(user = current_user, is_finished = False).order_by('-id')

        if len(order_list) > 0 :
            order = order_list[0]
        else:
            order = None
        document_list = Document.objects.filter(order = order)
        show_check = True
        print(document_list)

    # print(image_names)
    return render(request, 'relatedpages/show.html',
    {'show_check':show_check,
    'documents':document_list
    })

def delete(request):
    delete_check = False
    message = ''
    if request.method == 'POST':
        document_id = request.POST.get('id',0)
        current_user = request.user
        if document_id != 0:
            document = Document.objects.filter(id = document_id, user = current_user)
            if len(document) != 0:
                document[0].delete()
                delete_check = True
                message = 'your image deleted successfully'
            else:
                message = 'document not found'
        else:
            message = 'document not found'


    return JsonResponse({
    'status': delete_check,
    'message': message
    })
