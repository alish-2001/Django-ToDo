# Generated by Django 5.0.2 on 2024-04-16 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0006_task_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True),
        ),
    ]
