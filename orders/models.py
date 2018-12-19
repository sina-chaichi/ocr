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

class Document(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, default=None)
    document = models.FileField(upload_to='uploaded/')
    doc_name = models.UUIDField(default=uuid.uuid4, unique=True, max_length=512)
    uploaded_at = models.DateTimeField(default = now)

class Process(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, default=None)
    fileUpload = models.FileField(default=None, upload_to='proccessed/')
