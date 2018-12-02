from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from users.models import Document
from users.forms import DocumentForm
from django.urls import reverse



def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = DocumentForm()
    return render(request, 'relatedpages/upload.html', {
        'form': form
    })
