from django.urls import path,include

urlpatterns = [
    path('v1/users/', include('apps.users.urls')),
    path('v1/leaf/', include('apps.leaf.urls')), 
    path('v1/nutrition/', include('apps.nutrition.urls')),
]