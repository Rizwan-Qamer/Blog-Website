from django.db import models # type: ignore

class Blog(models.Model):
    Blog = models.CharField(max_length=200)
    description = models.TextField()

    # Optional: define a custom primary key
    # id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.Blog

    class Meta:
        managed = True  # Ensure Django manages this table (optional)


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    blog = models.ForeignKey(Blog, related_name='posts', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    class Meta:
        managed = True  # Ensure Django manages this table (optional)
