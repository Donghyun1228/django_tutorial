from django import forms
from .models import Post

# post 생성 및 업데이트를 위한 Form
class PostForm(forms.ModelForm):

    class Meta:

        model = Post
        fields = ['title', 'author', 'content']