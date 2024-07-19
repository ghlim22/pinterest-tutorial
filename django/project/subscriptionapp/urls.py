from django.urls import path
from django.views.generic import TemplateView

from . import views
from .views import SubscriptionListView, SubscriptionView

app_name = "subscriptionapp"

urlpatterns = [
    path("subscribe/", SubscriptionView.as_view(), name="subscribe"),
    path("list/", SubscriptionListView.as_view(), name="list"),
]
