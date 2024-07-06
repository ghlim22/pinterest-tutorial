from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = "projectapp"

urlpatterns = [
    path("list/", views.ProjectListView.as_view(), name="list"),
    path("create/", views.ProjectCreateView.as_view(), name="create"),
    path("detail/<int:pk>", views.ProjectDetailView.as_view(), name="detail"),
]
