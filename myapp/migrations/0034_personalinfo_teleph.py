# Generated by Django 3.0.14 on 2022-06-26 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0033_delete_personalinfo1'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalinfo',
            name='Teleph',
            field=models.CharField(default=False, max_length=50),
        ),
    ]
