# Generated by Django 3.2.9 on 2021-11-24 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_cryptoprice_last_refreshed'),
    ]

    operations = [
        migrations.AddField(
            model_name='cryptoprice',
            name='from_symbol',
            field=models.CharField(default='BTC', max_length=3),
        ),
        migrations.AddField(
            model_name='cryptoprice',
            name='to_symbol',
            field=models.CharField(default='USD', max_length=3),
        ),
    ]