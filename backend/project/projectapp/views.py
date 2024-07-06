from articleapp.models import Article
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.list import MultipleObjectMixin

from . import forms, models

# Create your views here.


@method_decorator(login_required, "get")
@method_decorator(login_required, "post")
class ProjectCreateView(CreateView):
    model = models.Project
    form_class = forms.ProjectCreationForm
    template_name = "projectapp/create.html"

    def get_success_url(self):
        return reverse("projectapp:detail", kwargs={"pk": self.object.pk})


class ProjectDetailView(DetailView, MultipleObjectMixin):
    model = models.Project
    context_object_name = "target_project"
    template_name = "projectapp/detail.html"
    paginate_by = 7

    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(project=self.get_object())
        return super(ProjectDetailView, self).get_context_data(object_list=object_list, **kwargs)


class ProjectListView(ListView):
    model = models.Project
    context_object_name = "project_list"
    template_name = "projectapp/list.html"
    paginate_by = 20
