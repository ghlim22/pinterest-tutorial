from django.forms import ModelForm

from . import models
class CommentCreationForm(ModelForm):
    class Meta:
        model = models.Comment
        fields = ['content']
