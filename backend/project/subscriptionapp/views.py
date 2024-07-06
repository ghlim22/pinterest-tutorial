from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView
from projectapp.models import Project

from . import models

# Create your views here.


@method_decorator(login_required, "get")
class SubscriptionView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse("projectapp:detail", kwargs={"pk": self.request.GET.get("project_pk")})

    def get(self, request, *args, **kwargs):

        project = get_object_or_404(Project, pk=self.request.GET.get("project_pk"))
        user = self.request.user
        sub = models.Subscription.objects.filter(user=user, project=project)
        # (user, project)의 구독이 존재하면 제거하고 없으면 새로 만든다.
        if sub.exists():
            sub.delete()
        else:
            models.Subscription(user=user, project=project).save()
        return super(SubscriptionView, self).get(request, *args, **kwargs)
