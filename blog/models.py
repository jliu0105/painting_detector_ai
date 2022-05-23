from django.db import models
from django.contrib.auth.models import User
#
# # Create your models here.
#
# class Category(models.Model):
#     name = models.CharField(max_length=150)
#
# class Tag(models.Model):
#     name = models.CharField(max_length=150)
#
#
# class Post(models.Model):
#     title = models.CharField(max_length=150)
#     body = models.TextField()
#     created_time = models.DateTimeField()
#     modified_time = models.DateTimeField()
#     excerpt = models.CharField(max_length=150, blank=True)
#
#     category = models.ForeignKey('Category',on_delete=models.CASCADE)
#     tags = models.ManyToManyField(Tag, blank=True)
#     author = models.ForeignKey(User,on_delete=models.CASCADE)

class user(models.Model):
    username = models.CharField(max_length=20)
    headImg = models.ImageField(upload_to='mysite/upload/')