# Generated by Django 5.1.2 on 2024-11-06 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog1', '0007_delete_comment_delete_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.CharField(choices=[('CricketBlog', 'Cricket'), ('NewsBlog', 'News')], default='CricketBlog', max_length=50),
        ),
    ]
