from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.TextField()
    cookie = models.BinaryField()  # A RequestsCookieJar object in requests
    cookie_last_update = models.DateTimeField()

    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.username}-{self.name}"
