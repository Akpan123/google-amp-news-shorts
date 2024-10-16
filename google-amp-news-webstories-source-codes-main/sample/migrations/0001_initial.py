# Generated by Django 4.0 on 2022-01-25 11:50

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('category', models.CharField(blank=True, max_length=100)),
                ('author', models.CharField(blank=True, max_length=100)),
                ('a_cover', models.ImageField(blank=True, null=True, upload_to='article_covers/')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('source', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('s_cover', models.ImageField(blank=True, null=True, upload_to='slides/')),
                ('article_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='slide_covers', to='sample.article')),
            ],
        ),
    ]
