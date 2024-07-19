from articleapp.models import Article
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView, DetailView, ListView
from django.views.generic.list import MultipleObjectMixin
from subscriptionapp.models import Subscription

from . import deco, forms, models

# Create your views here.

has_ownership = [login_required, deco.project_ownership_required]


@method_decorator(login_required, "get")
@method_decorator(login_required, "post")
class ProjectCreateView(CreateView):
    model = models.Project
    form_class = forms.ProjectCreationForm
    template_name = "projectapp/create.html"

    def form_valid(self, form):
        temp = form.save(commit=False)
        temp.owner = self.request.user
        temp.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("projectapp:detail", kwargs={"pk": self.object.pk})


class ProjectDetailView(DetailView, MultipleObjectMixin):
    model = models.Project
    context_object_name = "target_project"
    template_name = "projectapp/detail.html"
    paginate_by = 7

    # template에 넘길 context data를 준비한다.
    def get_context_data(self, **kwargs):
        project = self.object
        user = self.request.user
        if user.is_authenticated:
            sub = Subscription.objects.filter(user=user, project=project)
        else:
            sub = None
        object_list = Article.objects.filter(project=self.get_object())
        return super(ProjectDetailView, self).get_context_data(object_list=object_list, subscription=sub, **kwargs)


class ProjectListView(ListView):
    model = models.Project
    context_object_name = "project_list"
    template_name = "projectapp/list.html"
    paginate_by = 20

    def get_queryset(self):
        project_list = models.Project.objects.all().order_by("title")
        return project_list


# @method_decorator(has_ownership, "get")
# @method_decorator(has_ownership, "post")
class ProjectDeleteView(DeleteView):
    model = models.Project
    context_object_name = "target_project"
    success_url = reverse_lazy("projectapp:list")
    template_name = "projectapp/delete.ㅛyhtml"
