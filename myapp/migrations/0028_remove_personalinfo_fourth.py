# Generated by Django 3.0.14 on 2022-06-25 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0027_personalinfo_fourth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personalinfo',
            name='Fourth',
        ),
    ]