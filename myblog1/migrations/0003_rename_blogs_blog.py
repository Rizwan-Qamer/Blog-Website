# Generated by Django 5.1.2 on 2024-10-30 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog1', '0002_rename_blog_blogs'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Blogs',
            new_name='Blog',
        ),
    ]