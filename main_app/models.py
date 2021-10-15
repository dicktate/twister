from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    # def __str__(self):
    #     return '%i) %s' % (self.id, self.name)

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    time = models.DateTimeField('date published')
    def __str__(self):
        return self.text + ' ** '

class Tag(models.Model):
    post = models.ManyToManyField(Post)
    name = models.CharField(max_length=64)
