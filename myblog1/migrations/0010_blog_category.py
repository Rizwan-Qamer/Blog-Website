# Generated by Django 5.1.2 on 2024-11-08 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog1', '0009_remove_blog_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
