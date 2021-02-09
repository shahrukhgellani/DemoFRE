from django.db import models
# models.py
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import models


# private_storage = FileSystemStorage(location=settings.PRIVATE_STORAGE_ROOT)
#
# class MyModel(models.Model):
#     upload = models.FileField(upload_to='uploads/')
#
#     # or...
#
#     upload = models.FileField(upload_to='uploads/% Y/% m/% d/')
