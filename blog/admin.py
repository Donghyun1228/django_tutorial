from django.contrib import admin
from .models import Post
# Register your models here.

# admin site에서 Post 모델을 수정할 수 있도록 등록
admin.site.register(Post)