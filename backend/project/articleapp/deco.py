from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

from . import models


def article_ownership_required(func):
    def decorated(request, *args, **kwargs):
        article = models.Article.objects.get(pk=kwargs["pk"])
        if not article.writer == request.user:
            return HttpResponseForbidden()
        else:
            return func(request, *args, **kwargs)

    return decorated
