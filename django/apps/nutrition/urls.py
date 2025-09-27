from django.urls import path
from .views import loadNutrition, pageNutrition
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', pageNutrition, name='pageNutrition'),
    path('upload-nutrition/', loadNutrition, name='loadNutrition')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)