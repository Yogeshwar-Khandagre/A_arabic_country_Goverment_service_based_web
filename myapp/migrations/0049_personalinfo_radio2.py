# Generated by Django 3.0.14 on 2022-06-28 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0048_personalinfo_radio1'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalinfo',
            name='Radio2',
            field=models.CharField(default=50, max_length=50),
        ),
    ]