# Generated by Django 5.0.7 on 2024-07-30 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_message_receiver'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='replyStatus',
            field=models.BooleanField(default=False),
        ),
    ]