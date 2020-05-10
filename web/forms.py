from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post

        fields = {
            'title': forms.TextInput(attrs={"placeholder": "Введите название статьи"}),
            'text': forms.Textarea(),
            'cover': forms.ImageField(),
        }
