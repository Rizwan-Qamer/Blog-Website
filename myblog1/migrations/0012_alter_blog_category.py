# Generated by Django 5.1.2 on 2024-11-08 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog1', '0011_alter_blog_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.CharField(max_length=50, null=True),
        ),
    ]