# Generated by Django 5.0 on 2024-04-16 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_sarkari_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='railway',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='upsc',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='vyapam',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='railway',
            name='railway_url',
            field=models.URLField(default=1, help_text='Enter a valid URL', max_length=999),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='upsc',
            name='upsc_url',
            field=models.URLField(default=2, help_text='Enter a valid URL', max_length=999),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vyapam',
            name='vyapam_url',
            field=models.URLField(default=2, help_text='Enter a valid URL', max_length=999),
            preserve_default=False,
        ),
    ]
