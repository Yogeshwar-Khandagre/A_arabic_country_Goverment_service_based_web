# Generated by Django 3.0.14 on 2022-06-25 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_personalinfo_family'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalinfo',
            name='Mothername',
            field=models.CharField(default=False, max_length=50),
        ),
    ]
