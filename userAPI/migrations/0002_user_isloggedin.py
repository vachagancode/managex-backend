# Generated by Django 5.0 on 2024-01-04 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userAPI', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='isLoggedIn',
            field=models.BooleanField(default=False),
        ),
    ]
