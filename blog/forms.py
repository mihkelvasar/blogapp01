from django import forms
from django.db.models.base import Model
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Post, Tag, Comment


class CustomMMCF(forms.ModelMultipleChoiceField):
    def label_from_instance(self, tag):
        return "%s" % tag.tag_name

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["post_title", "post_content", "post_draft", "post_tags"]

    post_tags = CustomMMCF(
        queryset = Tag.objects.all(),
        widget = forms.CheckboxSelectMultiple
    )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["author", "author_mail", "com_content"]


class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)