# Generated by Django 5.1.1 on 2024-09-15 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0009_remove_post_image_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='subtitle',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
