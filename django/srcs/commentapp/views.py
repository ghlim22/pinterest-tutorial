from articleapp.models import Article
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView

from . import deco, forms, models

has_ownership = [login_required, deco.comment_ownership_required]


# Create your views here.


class CommentCreateView(CreateView):
    model = models.Comment
    form_class = forms.CommentCreationForm
    template_name = "commentapp/create.html"

    def form_valid(self, form):
        temp_comment = form.save(commit=False)
        temp_comment.article = Article.objects.get(pk=self.request.POST["article_pk"])
        temp_comment.writer = self.request.user
        temp_comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("articleapp:detail", kwargs={"pk": self.object.article.pk})


@method_decorator(has_ownership, "get")
@method_decorator(has_ownership, "post")
class CommentDeleteView(DeleteView):
    model = models.Comment
    context_object_name = "target_comment"
    template_name = "commentapp/delete.html"

    def get_success_url(self):
        return reverse("articleapp:detail", kwargs={"pk": self.object.article.pk})
