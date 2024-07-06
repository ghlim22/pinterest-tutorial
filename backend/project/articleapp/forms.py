from django.forms import ModelForm

from . import models


class ArticleCreationForm(ModelForm):
    class Meta:
        model = models.Article
        fields = ["title", "image", "project", "content"]
