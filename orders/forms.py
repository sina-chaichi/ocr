from django import forms
from orders.models import Document, Process

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('document',)

class ProcessForm(forms.ModelForm):
    class Meta:
        model = Process
        fields = ('user','order','fileUpload',)
