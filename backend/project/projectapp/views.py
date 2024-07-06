from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, ListView

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


class ProjectDetailView(DetailView):
    model = models.Project
    context_object_name = "target_project"
    template_name = "projectapp/detail.html"


class ProjectListView(ListView):
    model = models.Project
    context_object_name = "project_list"
    template_name = "projectapp/list.html"
    paginate_by = 20
