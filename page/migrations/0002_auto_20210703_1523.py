# Generated by Django 3.2.5 on 2021-07-03 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='pageimage'),
        ),
        migrations.AlterModelTable(
            name='post',
            table='page_post',
        ),
    ]
