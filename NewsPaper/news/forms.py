from django import forms
from django.core.exceptions import ValidationError

from .models import Post


class PostForm(forms.ModelForm):
    
    post_type = forms.ChoiceField(choices=Post.POST_TYPE)
    
    class Meta:
        model = Post
        fields = 'title', 'text', 'post_type', 'author'

    def clean(self):
        cleaned_data = super().clean()
        description = cleaned_data.get("text")
        name = cleaned_data.get("title")

        if name == description:
            raise ValidationError(
                "Описание не должно быть идентично названию."
            )

        return cleaned_data


class PostFilterForm(forms.Form):
    post_type = forms.ChoiceField(
        choices=[('__all__', 'Все')] + list(Post.POST_TYPE),
        required=False,
    )