# Generated by Django 3.2.5 on 2021-07-03 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0008_alter_post_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='time',
        ),
    ]
