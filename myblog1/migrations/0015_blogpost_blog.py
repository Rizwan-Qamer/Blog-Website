# Generated by Django 5.1.2 on 2024-11-14 12:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog1', '0014_remove_blogpost_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='blog',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='myblog1.blog'),
        ),
    ]