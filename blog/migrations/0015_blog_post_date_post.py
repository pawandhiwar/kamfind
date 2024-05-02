# Generated by Django 5.0.4 on 2024-04-23 06:44

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_blog_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_post',
            name='date_post',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
