# Generated by Django 5.0 on 2024-04-22 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_blog_post_tumnails_sarkari_post_tumnails_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_post',
            name='Tumnails',
            field=models.ImageField(blank=True, upload_to='static/all_images/'),
        ),
        migrations.AlterField(
            model_name='sarkari_post',
            name='Tumnails',
            field=models.ImageField(blank=True, upload_to='static/all_images/'),
        ),
        migrations.AlterField(
            model_name='sec_post',
            name='Tumnails',
            field=models.ImageField(blank=True, upload_to='static/all_images/'),
        ),
        migrations.AlterField(
            model_name='top_job',
            name='Tumnails',
            field=models.ImageField(blank=True, upload_to='static/all_images/'),
        ),
    ]