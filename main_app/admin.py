from django.contrib import admin

# Register your models here.
from .models import Post, MyUser, Tag

admin.site.register(Post)
admin.site.register(MyUser)
admin.site.register(Tag)