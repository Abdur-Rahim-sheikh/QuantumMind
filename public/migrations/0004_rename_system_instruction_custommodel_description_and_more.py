# Generated by Django 5.0.6 on 2024-06-13 15:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0003_alter_chatsession_conversations_custommodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='custommodel',
            old_name='system_instruction',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='custommodel',
            old_name='model_name',
            new_name='name',
        ),
        migrations.AddField(
            model_name='custommodel',
            name='age',
            field=models.IntegerField(default=18),
        ),
        migrations.AddField(
            model_name='custommodel',
            name='avatar',
            field=models.TextField(blank=True, help_text='Base64 image of the avatar', null=True),
        ),
        migrations.AddField(
            model_name='custommodel',
            name='gender',
            field=models.CharField(default='neutral', max_length=100),
        ),
        migrations.AddField(
            model_name='custommodel',
            name='language',
            field=models.CharField(default='en', max_length=100),
        ),
        migrations.AddField(
            model_name='custommodel',
            name='private',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='custommodel',
            name='status',
            field=models.CharField(default='active', max_length=100),
        ),
        migrations.AlterField(
            model_name='chatsession',
            name='conversations',
            field=models.JSONField(default=list),
        ),
        migrations.CreateModel(
            name='BotFriend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conversations', models.JSONField(default=list)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('custom_model', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='public.custommodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
