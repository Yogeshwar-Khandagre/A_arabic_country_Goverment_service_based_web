# Generated by Django 3.0.14 on 2022-07-01 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0065_user8'),
    ]

    operations = [
        migrations.CreateModel(
            name='User9',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(max_length=50)),
                ('Password', models.CharField(max_length=50)),
            ],
        ),
    ]