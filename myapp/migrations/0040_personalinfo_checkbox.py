# Generated by Django 3.0.14 on 2022-06-26 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0039_auto_20220626_1956'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalinfo',
            name='checkbox',
            field=models.BooleanField(default=True),
        ),
    ]
