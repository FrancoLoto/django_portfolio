from django.db import models

class Post(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    image = models.ImageField(upload_to='blog/images')
    created_at = models.DateTimeField(auto_now_add=True)
