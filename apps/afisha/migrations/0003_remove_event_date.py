# Generated by Django 3.2.12 on 2022-02-25 23:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('afisha', '0002_event_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='date',
        ),
    ]