# Generated by Django 2.0.5 on 2018-07-20 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xasdb1', '0018_auto_20180710_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='xasmode',
            name='mode',
            field=models.SmallIntegerField(choices=[(-1, 'Unknown'), (0, 'Transmission'), (1, 'Fluorescence'), (2, 'Fluorescence, unitstep'), (3, 'Normalized absorption spectrum')], default=-1),
        ),
    ]
