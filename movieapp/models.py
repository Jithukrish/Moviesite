from django.db import models

class Post(models.Model):
    title=models.CharField(max_length=200)
    slug=models.SlugField(unique=True,max_length=200)
    created_on=models.DateTimeField(auto_now_add=True)
