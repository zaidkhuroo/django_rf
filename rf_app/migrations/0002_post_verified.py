# Generated by Django 5.0.6 on 2024-07-10 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rf_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='verified',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
