from django.urls import path
from django.views.generic import TemplateView

from . import views
from .views import SubscriptionView

app_name = "subscriptionapp"

urlpatterns = [path("subscribe/", SubscriptionView.as_view(), name="subscribe")]
