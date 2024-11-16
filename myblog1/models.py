from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    
                                      
    def __str__(self):
        return self.title
    
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    blog = models.ForeignKey(Blog, related_name='posts', on_delete=models.CASCADE, null=True)
                                      
    def __str__(self):
        return self.title
    