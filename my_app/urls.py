from django.urls import path
from my_app.views import *


urlpatterns = [
    path('trans/', trans),
    path('ocr_text/', OCR),
    path('station/', statiom)
]
