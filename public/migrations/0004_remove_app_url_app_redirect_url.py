# Generated by Django 5.0.6 on 2024-05-18 17:12

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0003_remove_app_redirect_uri_account_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='app',
            name='url',
        ),
        migrations.AddField(
            model_name='app',
            name='redirect_url',
            field=models.CharField(default=django.utils.timezone.now, help_text='Url for the app', max_length=100),
            preserve_default=False,
        ),
    ]
