from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=128, null=False)
    image = models.ImageField(upload_to="projects/", null=False)
    description = models.TextField(null=False)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.pk}: {self.title}"
