# Generated by Django 5.2.1 on 2025-05-26 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes_app', '0002_rename_note_note_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='is_marked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='note',
            name='is_trash',
            field=models.BooleanField(default=False),
        ),
    ]
