# Generated by Django 3.2 on 2022-04-12 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0016_remove_event_ticket_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='user',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]