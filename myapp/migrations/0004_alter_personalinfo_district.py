# Generated by Django 3.2.13 on 2022-06-25 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_personalinfo_district'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalinfo',
            name='district',
            field=models.CharField(max_length=50),
        ),
    ]