# Generated by Django 4.0 on 2022-02-04 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0005_remove_article_author_alter_article_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
