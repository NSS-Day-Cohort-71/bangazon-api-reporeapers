from django.db import models
from django.contrib.auth.models import User


class Store(models.Model):

    seller = models.ForeignKey(User, on_delete=models.DO_NOTHING,)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)