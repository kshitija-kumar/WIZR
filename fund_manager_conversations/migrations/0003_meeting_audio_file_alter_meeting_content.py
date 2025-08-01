# Generated by Django 5.2.4 on 2025-07-30 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fund_manager_conversations', '0002_meeting_pdf_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='audio_file',
            field=models.FileField(blank=True, null=True, upload_to='meeting_audio/'),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='content',
            field=models.TextField(blank=True),
        ),
    ]
