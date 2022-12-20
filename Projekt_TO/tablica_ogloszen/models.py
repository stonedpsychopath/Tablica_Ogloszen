from django.db import models
from django.contrib.auth.models import AbstractUser



class Categories(models.Model):
    class Meta:
       verbose_name = 'Categories'
       verbose_name_plural = 'Categories'

    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name

class Announcement(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=200)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.name

class Comments(models.Model):

    class Meta:
       verbose_name = 'Comment'
       verbose_name_plural = 'Comments'

    name = models.CharField(max_length=200)
    likes = models.IntegerField(default=0)
    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    phoneNumber = models.CharField(max_length=9)


