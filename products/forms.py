from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Write your thoughts about this coffee...',
                'class': 'form-control',
                'style': 'background-color: #f4e6cd;'
            }),
        }