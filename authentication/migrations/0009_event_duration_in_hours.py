# Generated by Django 4.0.3 on 2022-04-24 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_event_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='duration_in_hours',
            field=models.IntegerField(default=4),
            preserve_default=False,
        ),
    ]
