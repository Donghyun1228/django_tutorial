from django.db import models

# Create your models here.
class Post(models.Model):
    post_title = models.CharField(max_length=200)
    def __str__(self):
        return self.post_title

