# Generated by Django 3.2.13 on 2022-06-25 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_personalinfo_ministry'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalinfo',
            name='Area',
            field=models.CharField(default=False, max_length=50),
        ),
    ]
