from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = "commentapp"

urlpatterns = [
    path("create/", views.CommentCreateView.as_view(), name="create"),
    path("delete/<int:pk>", views.CommentDeleteView.as_view(), name="delete"),
]
