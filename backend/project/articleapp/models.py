from django.contrib.auth.models import User
from django.db import models
from projectapp.models import Project


# Create your models here.
class Article(models.Model):
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, related_name="article", null=True)
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="article", null=True)
    title = models.CharField(max_length=128, null=True)
    image = models.ImageField(upload_to="article/", null=False)
    content = models.TextField(null=True)
    created_at = models.DateField(auto_now_add=True, null=True)
