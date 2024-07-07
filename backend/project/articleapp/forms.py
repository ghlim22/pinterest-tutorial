from django import forms
from django.forms import ModelForm
from projectapp.models import Project

from . import models


class ArticleCreationForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={"class": "editable text-left", "style": "height: auto;"}))
    project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False)

    class Meta:
        model = models.Article
        fields = ["title", "image", "project", "content"]
