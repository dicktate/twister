from django.db import models

# Create your models here.
class Post(models.Model):
    text = models.CharField(max_length=200)
    time = models.DateTimeField('date published')
    def __str__(self):
        return self.text

class User(models.Model):
    name = models.CharField(max_length=128)
    key = models.CharField(max_length=128)

class Tag(models.Model):
    post = models.ManyToManyField(Post)
    name = models.CharField(max_length=64)

