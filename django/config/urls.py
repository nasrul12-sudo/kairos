from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

def landingPage(request): return render(request, 'index.html')
def starterPage(request): return render(request, 'starter-page.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.api.urls')),

    path('', landingPage, name='home'),
    path('starter-page/', starterPage, name='starter'),

    path('dashboard/', include('apps.dashboard.urls')),
    path('user/', include("apps.users.urls")),
    path('leaf/', include("apps.leaf.urls")),
    path('nutrition/', include("apps.nutrition.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
