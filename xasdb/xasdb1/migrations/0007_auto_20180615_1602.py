# Generated by Django 2.0.5 on 2018-06-15 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xasdb1', '0006_auto_20180612_1141'),
    ]

    operations = [
        migrations.AddField(
            model_name='xasfile',
            name='beamline_name',
            field=models.CharField(default='unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='xasfile',
            name='facility_name',
            field=models.CharField(default='unknown', max_length=100),
        ),
    ]
