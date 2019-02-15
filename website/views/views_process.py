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


def process(request):
    procces_check = False
    if request.method == 'POST':
        current_user = request.user
        order_list = Order.objects.filter(user = current_user, is_finished = False).order_by('-id')
        for current_order in order_list:

            doc_list = Document.objects.filter(order = current_order).order_by('uploaded_at')
            doc_num = 0
            # image = [None]*len(doc_list)
            txt = [None]*len(doc_list)
            file_names = []
            for doc in doc_list:
                doc_process = doc.document.name
                doc_path = str(doc_process)
                image = Image.open('/home/sina/work/ocr/ocr/website/media/'+doc_path)
                image.filter(ImageFilter.SHARPEN)
                txt[doc_num] = pytesseract.image_to_string(
                image,
                lang='eng')
                # create txt file to ubsert processed image texts

                file_name = '/home/sina/work/ocr/ocr/website/media/processed/text{}-{}-{}.txt'.format(doc.id,current_user.id,current_order.id)
                if not os.path.exists(os.path.dirname(file_name)):
                    try:
                        os.makedirs(os.path.dirname(file_name))
                    except OSError as exc: # Guard against race condition
                        if exc.errno != errno.EEXIST:
                            raise
                with open(file_name, "w") as f:
                    f.write(txt[doc_num])
                file_names.append(file_name)
                print(doc_num)
                doc_num = doc_num + 1
        current_order.is_finished = True
        current_order.save()
        procces_check = True
        return JsonResponse({
        'status':'ok',
        'files' : file_names
        })
    else:
        return HttpResponse('Here is no valid request')
    return render(request, 'relatedpages/process.html', {
            'procces_check':procces_check
        })
