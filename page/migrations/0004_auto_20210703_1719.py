# Generated by Django 3.2.5 on 2021-07-03 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0003_auto_20210703_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='canton',
            field=models.CharField(default='-', max_length=255),
        ),
        migrations.AlterField(
            model_name='post',
            name='country',
            field=models.CharField(default='-', max_length=255),
        ),
        migrations.AlterField(
            model_name='post',
            name='district',
            field=models.CharField(default='-', max_length=255),
        ),
        migrations.AlterField(
            model_name='post',
            name='lcanton',
            field=models.CharField(default='-', max_length=255),
        ),
        migrations.AlterField(
            model_name='post',
            name='ldistrict',
            field=models.CharField(default='-', max_length=255),
        ),
    ]