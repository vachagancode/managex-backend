# Generated by Django 5.0 on 2024-01-12 17:22

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userAPI', '0007_remove_task_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='owner',
            field=models.TextField(default=django.utils.timezone.now),
        ),
    ]