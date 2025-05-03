# guestbook/urls.py
from django.urls import path
from .views import guestbook_api

urlpatterns = [
    path('', guestbook_api, name='guestbook_api'),
]
