from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """
    A model representing user profile information.

    Attributes:
        user (User): A one-to-one relationship to the built-in Django User model.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
