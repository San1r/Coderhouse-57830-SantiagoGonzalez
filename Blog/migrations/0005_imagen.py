# Generated by Django 5.1.1 on 2024-09-14 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0004_post_image_alter_post_published_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='imagenes')),
                ('descripcion', models.CharField(max_length=255)),
            ],
        ),
    ]
