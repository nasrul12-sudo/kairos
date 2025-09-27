from django.urls import path
from .views import loadLeaf, pageLeaf
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', pageLeaf, name='Loadleaf'),
    path('upload-leaf/', loadLeaf, name='pageLeaf')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)