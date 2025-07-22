from django.db import models

class GuestMessage(models.Model):
    author = models.CharField(max_length=50)
    belonging = models.CharField(max_length=15)
    message = models.TextField()
    written_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'이름: {self.author} | 소속: {self.belonging} | 메시지: {self.message}'
