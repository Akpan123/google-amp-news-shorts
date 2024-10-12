# Generated by Django 4.0 on 2022-01-26 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0003_remove_slide_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slide',
            old_name='article_name',
            new_name='article',
        ),
        migrations.RemoveField(
            model_name='article',
            name='category',
        ),
        migrations.RemoveField(
            model_name='slide',
            name='source',
        ),
        migrations.RemoveField(
            model_name='slide',
            name='title',
        ),
        migrations.AddField(
            model_name='slide',
            name='content',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='slide',
            name='is_p',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
