# Generated by Django 5.0 on 2024-04-22 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_alter_blog_post_tumnails_alter_sarkari_post_tumnails_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_post',
            name='Tumnails',
            field=models.ImageField(blank=True, null=True, upload_to='static/all_images/'),
        ),
    ]