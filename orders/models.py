from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone
import uuid
from datetime import datetime
from django.utils.timezone import now

# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    is_finished = models.BooleanField(default=False)
    created_at = models.DateTimeField(default = now)
    updated_at = models.DateTimeField(default = now)

    def __str__(self):
        return ('order by user {}'.format(self.user))

class Document(models.Model):
    def upload_to(instnce,doc_name):
        return 'uploaded/{0}'.format(instnce.doc_name)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, default=None)
    doc_name = models.UUIDField(default=uuid.uuid4, unique=True, max_length=512)
    document = models.FileField(upload_to= upload_to)
    uploaded_at = models.DateTimeField(default = now)

    def __str__(self):
        return ('uploaded at {} by user {}'.format(self.uploaded_at,self.user))


class Process(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, default=None)
    fileUpload = models.FileField(default=None, upload_to='proccessed/')

    def __str__(self):
        return self.user
