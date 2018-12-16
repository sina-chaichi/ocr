from django import forms
from orders.models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('document',)
