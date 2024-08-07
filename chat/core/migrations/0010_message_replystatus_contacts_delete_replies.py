# Generated by Django 5.0.7 on 2024-07-30 07:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_remove_message_replystatus_replies_delete_contacts'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='replyStatus',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts_1', to=settings.AUTH_USER_MODEL)),
                ('userId2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts_2', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Replies',
        ),
    ]
