# Generated by Django 5.0.7 on 2024-08-01 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_message_messagefirst14_alter_message_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='messagefirst14',
        ),
    ]
