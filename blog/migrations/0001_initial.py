# Generated by Django 5.0.1 on 2024-01-19 11:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('img_id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='gallery/')),
                ('add_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Packages',
            fields=[
                ('pack_id', models.AutoField(primary_key=True, serialize=False)),
                ('pack_img', models.ImageField(upload_to='packages/')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.CharField(max_length=20)),
                ('url', models.CharField(max_length=50)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('service_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('add_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('url', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Trips',
            fields=[
                ('trip_id', models.AutoField(primary_key=True, serialize=False)),
                ('destination', models.CharField(max_length=100)),
                ('departure', models.DateTimeField(null=True)),
                ('arrival', models.DateTimeField(null=True)),
                ('review', models.TextField()),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]