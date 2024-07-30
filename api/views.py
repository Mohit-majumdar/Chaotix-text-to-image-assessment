from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .tasks import generate_image
from logging import Logger

logger = Logger(__name__)


class GenerateImageView(APIView):
    def post(self, request):
        try:
            prompts = request.data.get("prompt")
            task_ids = [generate_image.delay(prompt).id for prompt in prompts]
            return Response({"task_ids": task_ids})
        except Exception as e:
            logger.log(1, "got error in views %s", str(e))
            return Response("INTERNAL SERVER ERROR", status=500)
