# Generated by Django 3.2 on 2022-04-12 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0017_alter_event_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='user',
        ),
    ]
