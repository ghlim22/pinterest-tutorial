from django.db import models


class TestProfile(models.Model):
    text = models.CharField(max_length=255, null=False)


# Create your models here.
