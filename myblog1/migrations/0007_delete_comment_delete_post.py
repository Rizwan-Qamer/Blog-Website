# Generated by Django 5.1.2 on 2024-11-04 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog1', '0006_post_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
