from django.shortcuts import render

from django.views.generic import CreateView

from . import forms
from . import models


# Create your views here.

class CommentCreateView(CreateView):
    model = models.Comment
