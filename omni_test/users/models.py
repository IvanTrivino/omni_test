# Django imports
# from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    class Meta(AbstractUser.Meta):
        db_table = 'users'
