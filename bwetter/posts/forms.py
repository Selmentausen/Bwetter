from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    text = forms.CharField(
        required=True, max_length=512,
        widget=forms.widgets.Textarea(attrs={
            'placeholder': 'Bweet something!',
            'class': 'textarea is-success is-medium',
            'label': ''
        })
    )
    title = forms.CharField(
        required=True, max_length=64,
        widget=forms.widgets.TextInput(attrs={
            'placeholder': 'Title of your bweet...',
            'class': 'input is-success',
            'label': ''
        })
    )

    class Meta:
        model = Post
        exclude = ("user",)
