from django.db import models
from file_storage.utils import BaseModel

from core.handlers import file_upload_handler
import secrets


class File(BaseModel):
    file = models.FileField(upload_to=file_upload_handler)
    slug = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = secrets.token_hex(10)

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.file.delete()
        return super().delete(*args, **kwargs)

    def __str__(self):
        return self.name
