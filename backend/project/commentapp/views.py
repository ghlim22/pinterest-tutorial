from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView

from . import forms, models

# Create your views here.


class CommentCreateView(CreateView):
    model = models.Comment
    form_class = forms.CommentCreationForm
    template_name = "commentapp/create.html"

    def form_valid(self, form):
        return super

    def get_success_url(self):
        return reverse("articleapp:detail", kwargs={"pk": self.object.article.pk})
