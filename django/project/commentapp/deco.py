from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

from . import models


def comment_ownership_required(func):
    def decorated(request, *args, **kwargs):
        comment = models.Comment.objects.get(pk=kwargs["pk"])
        if comment.writer == request.user:
            return func(request, *args, **kwargs)
        return HttpResponseForbidden()

    return decorated
