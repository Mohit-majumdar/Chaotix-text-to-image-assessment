import requests
from .models import ImageMetadata
from decouple import config
from celery import shared_task
from django.core.files.base import ContentFile
from logging import Logger

logger = Logger(__name__)

STABILITY_API_URL = config("STABILITY_API_URL", default="")
STABILITY_API_KEY = config("STABILITY_API_KEY")


@shared_task
def generate_image(prompt: str):
    try:
        headers = {
            "Authorization": f"Bearer {STABILITY_API_KEY}",
            "accept": "image/*",
        }
        data = {"prompt": prompt, "output_format": "jpeg", "model": "sd3-medium"}
        files = {
            "none": ""
            # Add other necessary fields and files as required by the API
        }

        # check prompt already in database or not
        image_obj = ImageMetadata.objects.filter(prompt=prompt)

        if image_obj:
            return image_obj.image.url

        response = requests.post(
            STABILITY_API_URL, data=data, files=files, headers=headers
        )
        print(response)
        if response.status_code == 200:
            print("creating image")
            generated_image = ImageMetadata(prompt=prompt)
            generated_image.image.save(prompt, ContentFile(response.content))
            generated_image.save()
            return generated_image.image.url
    except Exception as e:
        logger.log(1, "goet error while getting data from api %s", e)
