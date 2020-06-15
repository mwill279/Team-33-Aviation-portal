# Generated by Django 3.0.6 on 2020-06-02 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listapp', '0002_auto_20200602_1622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='choice',
        ),
        migrations.AddField(
            model_name='job',
            name='Jobtype',
            field=models.CharField(blank=True, choices=[('F', 'Full Time'), ('P', 'Part Time'), ('I', 'Internship')], max_length=1),
        ),
    ]