# Generated by Django 3.2.6 on 2021-08-27 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_rename_mocie_images_movie_movie_images'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='movie_images',
            new_name='movie_image',
        ),
    ]
