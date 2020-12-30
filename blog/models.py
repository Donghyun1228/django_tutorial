from django.db import models

# Create your models here.

# Post 모델 - 제목, 작가, 날짜, 내용의 attribute를 가지고 있음
class Post(models.Model):
    
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=10)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    # instance를 표시할 때 제목으로 표시
    def __str__(self):
        return self.title
