# Generated by Django 2.0.2 on 2018-04-28 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0002_auto_20180428_0918'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='age',
            field=models.IntegerField(default='0'),
        ),
    ]