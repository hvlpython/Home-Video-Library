# Generated by Django 3.2.6 on 2021-08-28 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_auto_20210828_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.ForeignKey(blank=True, default=None, max_length=128, null=True, on_delete=django.db.models.deletion.CASCADE, to='movies.genre'),
        ),
    ]
