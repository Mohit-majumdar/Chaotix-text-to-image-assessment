from django.urls import path
from .views import GenerateImageView

urlpatterns = [
    path("generate-images/", GenerateImageView.as_view(), name="generate-images"),
]
