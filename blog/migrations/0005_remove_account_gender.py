# Generated by Django 5.0.1 on 2024-01-21 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_account_about'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='gender',
        ),
    ]
