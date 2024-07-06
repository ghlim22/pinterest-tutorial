from django.forms import ModelForm

from . import models


class ProjectCreationForm(ModelForm):
    class Meta:
        model = models.Project
        fields = ["title", "image", "description"]
