# Generated by Django 3.2.9 on 2021-11-23 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_cryptoprice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cryptoprice',
            name='last_refreshed',
        ),
    ]
