# Generated by Django 3.0.6 on 2020-05-23 23:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aviation_portal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='image',
        ),
    ]