# Generated by Django 5.1.5 on 2025-02-25 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendar_events', '0002_alter_event_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
