# Generated by Django 4.2.5 on 2024-01-04 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie_rating', '0004_alter_movie_average_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie_rating.movie')),
            ],
        ),
    ]