from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'cover')

        fields = {
            'title': forms.TextInput(attrs={'placeholder': 'Введите название статьи'}),
            'text': forms.Textarea(),
            'cover': forms.ImageField(),
        }

        # fields = ('title placeholder="Введите название статьи"', 'text',)
        # widgets = {
        #     'name': forms.TextInput(attrs={'placeholder': 'Name'}),
        #     'description': forms.Textarea(
        #         attrs={'placeholder': 'Enter description here'}),
        # }
