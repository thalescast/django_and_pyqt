from django.db import models


class ModelUploadFile(models.Model):
    file = models.FileField('Realizar upload', upload_to='upload/')
