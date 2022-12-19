from django.db import models
from django.contrib.auth.models import AbstractUser

class Categories(models.Model):
    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name

class Announcement(models.Model):
    description = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True)


class Comments(models.Model):

    class Meta:
       verbose_name = 'Comment'
       verbose_name_plural = 'Comments'

    name = models.CharField(max_length=200)
    likes = models.IntegerField(default=0)
    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE, null=True)


# class User(models.Model):
#     name = models.CharField(max_length=200)
#     surname = models.CharField(max_length=200)
#     emailAddress = models.CharField(max_length=200)
#     phoneNumber = models.IntegerField()


class CustomUser(AbstractUser):
    phoneNumber = models.IntegerField(null=True)

