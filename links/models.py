from django.db import models
from django.utils import timezone
# Create your models here.

class Tag(models.Model):
    author = models.ForeignKey('auth.user')
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title