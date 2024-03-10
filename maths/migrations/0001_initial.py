# Generated by Django 4.2.11 on 2024-03-08 09:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answer', models.TextField()),
                ('hint', models.TextField(blank=True)),
                ('timer', models.PositiveIntegerField(blank=True, null=True)),
                ('animation', models.FilePathField(blank=True, choices=[('explode', 'explode'), ('fly_away', 'fly_away')], null=True, path='static/maths/animations')),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('time_last_edited', models.DateTimeField(auto_now=True)),
                ('categories', models.ManyToManyField(related_name='Problems', to='maths.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='problems', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProblemSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', models.TextField(blank=True)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('time_last_edited', models.DateTimeField(auto_now=True)),
                ('problems', models.ManyToManyField(related_name='problem_sets', to='maths.problem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='problem_sets', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
