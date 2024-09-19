# blog/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post,Comment
from taggit.forms import TagField 


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


#number 4
# blog/forms.py
from django import forms
from .models import Post
from taggit.forms import TagField, TagWidget  # Importing TagField and TagWidget
from taggit.managers import TaggableManager

class PostForm(forms.ModelForm):
    tags = TagField(widget=TagWidget(attrs={'placeholder': 'Add tags (comma-separated)'}))  # Use TagWidget

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # Include 'tags' in the fields







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

