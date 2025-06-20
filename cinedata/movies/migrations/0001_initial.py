# Generated by Django 5.2.3 on 2025-06-13 04:12

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.SlugField(default=uuid.uuid4, unique=True)),
                ('active_status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=30)),
                ('age', models.DateField()),
                ('photo', models.ImageField(upload_to='artists/')),
                ('proffession', models.CharField(choices=[('Actor', 'Actor'), ('Actress', 'Actress'), ('Director', 'Director'), ('Music Director', 'Music Director'), ('Producer', 'Producer'), ('Writer', 'Writer')], max_length=20)),
                ('industry', models.CharField(choices=[('Bollywood', 'Bollywood'), ('Hollywood', 'Hollywood'), ('Kollywood', 'Kollywood'), ('Tollywood', 'Tollywood'), ('Pollywood', 'Pollywood'), ('Sandalwood', 'Sandalwood'), ('Mollywood', 'Mollywood'), ('Others', 'Others')], max_length=20)),
            ],
            options={
                'verbose_name': 'Artist',
                'verbose_name_plural': 'Artist',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.SlugField(default=uuid.uuid4, unique=True)),
                ('active_status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Genre',
                'verbose_name_plural': 'Genre',
            },
        ),
        migrations.CreateModel(
            name='Production',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.SlugField(default=uuid.uuid4, unique=True)),
                ('active_status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('comp_name', models.CharField(max_length=30)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.artist')),
            ],
            options={
                'verbose_name': 'Production',
                'verbose_name_plural': 'Production',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.SlugField(default=uuid.uuid4, unique=True)),
                ('active_status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=30)),
                ('released_year', models.CharField(max_length=4)),
                ('runtime', models.TimeField()),
                ('description', models.TextField()),
                ('industry', models.CharField(choices=[('Bollywood', 'Bollywood'), ('Hollywood', 'Hollywood'), ('Kollywood', 'Kollywood'), ('Tollywood', 'Tollywood'), ('Pollywood', 'Pollywood'), ('Sandalwood', 'Sandalwood'), ('Mollywood', 'Mollywood'), ('Others', 'Others')], max_length=20)),
                ('photo', models.ImageField(upload_to='movies/')),
                ('cast', models.ManyToManyField(related_name='cast', to='movies.artist')),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='director', to='movies.artist')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.genre')),
                ('music_director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='music_director', to='movies.artist')),
                ('production', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='production', to='movies.production')),
            ],
            options={
                'verbose_name': 'Movie',
                'verbose_name_plural': 'Movies',
            },
        ),
    ]
