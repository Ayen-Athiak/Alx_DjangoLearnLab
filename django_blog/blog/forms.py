# blog/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post,Comment


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


from django import forms
from .models import Post
from taggit.forms import TagField  # Import TagField from django-taggit

class PostForm(forms.ModelForm):
    tags = TagField()  # Use TagField to create the tags field

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # Include 'tags' in the fields

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['tags'].widget.attrs.update({'placeholder': 'Add tags (comma-separated)'})







# number 3

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if not content:
            raise forms.ValidationError("Content cannot be empty.")
        return content

