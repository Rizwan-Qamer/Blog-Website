# models.py
from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        managed = True


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    blog = models.ForeignKey(Blog, related_name='posts', on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)  # Added image field

    def __str__(self):
        return self.title

    class Meta:
        managed = True
