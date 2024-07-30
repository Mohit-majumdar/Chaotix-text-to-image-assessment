from operator import mod
from django.db import models

# Create your models here.
#


class ImageMetadata(models.Model):
    prompt = models.TextField(null=True)
    image = models.ImageField(upload_to="generated_images/")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.prompt}"
