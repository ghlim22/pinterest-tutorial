from commentapp.forms import CommentCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from django.views.generic.edit import FormMixin

from . import deco, forms, models

has_ownership = [login_required, deco.article_ownership_required]


# Create your views here.


@method_decorator(login_required, "get")
@method_decorator(login_required, "post")
class ArticleCreateView(CreateView):
    model = models.Article
    form_class = forms.ArticleCreationForm
    template_name = "articleapp/create.html"

    def form_valid(self, form):
        temp_article = form.save(commit=False)
        temp_article.writer = self.request.user
        temp_article.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("articleapp:detail", kwargs={"pk": self.object.pk})


class ArticleDetailView(DetailView, FormMixin):
    model = models.Article
    context_object_name = "target_article"
    template_name = "articleapp/detail.html"
    form_class = CommentCreationForm


@method_decorator(has_ownership, "get")
@method_decorator(has_ownership, "post")
class ArticleUpdateView(UpdateView):
    model = models.Article
    context_object_name = "target_article"
    form_class = forms.ArticleCreationForm
    template_name = "articleapp/update.html"

    def get_success_url(self):
        return reverse("articleapp:detail", kwargs={"pk": self.object.pk})


@method_decorator(has_ownership, "get")
@method_decorator(has_ownership, "post")
class ArticleDeleteView(DeleteView):
    model = models.Article
    context_object_name = "target_article"
    success_url = reverse_lazy("articleapp:list")
    template_name = "articleapp/delete.html"


class ArticleListView(ListView):
    model = models.Article
    context_object_name = "article_list"
    template_name = "articleapp/list.html"
    paginate_by = 20

    def get_queryset(self):
        article_list = models.Article.objects.all().order_by("created_at")
        return article_list
