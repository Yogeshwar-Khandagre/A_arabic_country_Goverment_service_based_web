# Generated by Django 3.0.14 on 2022-06-25 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_personalinfo_disability'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalinfo',
            name='Apartment',
            field=models.CharField(default=False, max_length=50),
        ),
    ]
