# preapply/models.py
from django.db import models

class Application(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    sessions = models.JSONField(default=list, blank=True, null=True)

    def __str__(self):
        return f'이름: {self.name} | 메일: {self.email} | 연락처: {self.phone} | 세션: {self.sessions}'
