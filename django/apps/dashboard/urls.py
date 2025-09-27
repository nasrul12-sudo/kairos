from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.landingPage, name='home'),
    # path('chose/<str:modul_name', views.chose_module, name='chose_module')
]