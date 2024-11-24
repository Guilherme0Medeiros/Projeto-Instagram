from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image', 'caption']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Digite o título do post...'}),
            'caption': forms.Textarea(attrs={
                'placeholder': 'Escreva uma legenda...',
                'rows': 3,
                'style': 'resize:none;',
            }),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']  # Aqui você pode definir quais campos quer que o usuário preencha
