# preapply/urls.py
from django.urls import path
from .views import application_api

urlpatterns = [
    path('', application_api, name='application_api'),
]
