from django.db import models

class GuestMessage(models.Model):
    author = models.CharField(max_length=50)       # 이름
    message = models.TextField()                   # 메시지
    written_at = models.DateTimeField(auto_now_add=True)  # 작성 시간 (자동 저장)

    def __str__(self):
        return f'이름: {self.author} | 메시지: {self.message}'
