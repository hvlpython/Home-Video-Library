# Generated by Django 3.2.6 on 2021-08-27 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='mocie_images',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
