from django.db import models
from django.contrib.auth.models import AbstractUser

class Comments(models.Model):
    name = models.CharField(max_length=200)
    likes = models.IntegerField(default=0)


class Categories(models.Model):
    name = models.CharField(max_length=200)

class User(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    emailAddress = models.CharField(max_length=200)
    phoneNumber = models.IntegerField(max_length=12)

class Announcement(models.Model):
    description = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
class CustomUser(AbstractUser):
        pass
