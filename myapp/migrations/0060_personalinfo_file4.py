# Generated by Django 3.0.14 on 2022-06-30 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0059_remove_personalinfo_fille'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalinfo',
            name='File4',
            field=models.CharField(default=True, max_length=255),
        ),
    ]
