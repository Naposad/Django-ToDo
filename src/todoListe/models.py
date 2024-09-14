from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model
from django.utils.text import slugify


# Create your models here.


class TodoListe(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    slug = models.CharField(max_length=150)
    date_on = models.DateTimeField(default=datetime.now)
    date_end = models.DateTimeField(default=datetime.now)
    completed = models.BooleanField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
