# Generated by Django 3.0.14 on 2022-06-25 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_personalinfo_telephone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalinfo',
            name='Telephone',
            field=models.IntegerField(default=False),
        ),
    ]