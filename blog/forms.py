from django import forms
from .models import Post

# post 생성 및 업데이트를 위한 Form
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'author', 'content']
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Title',
                    'required data-validation-required-message': 'Please enter your title.' 
                }
            ),

            'author': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Author',
                    'required data-validation-required-message': 'Please enter the author.'
                }
            ),

            'content': forms.Textarea(
                attrs={
                    'rows': '5',
                    'class': 'form-control',
                    'required data-validation-required-message': 'Please enter your content.',
                    'area-invalid': 'true'
                }
            ),
        }