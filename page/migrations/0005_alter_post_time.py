# Generated by Django 3.2.5 on 2021-07-03 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0004_auto_20210703_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='time',
            field=models.CharField(default='-', max_length=255),
        ),
    ]
