# Generated by Django 2.2.1 on 2019-08-12 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xasdb1', '0026_xasuploadauxdata_aux_thumbnail_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='xasuploadauxdata',
            name='aux_thumbnail_file',
        ),
        migrations.AddField(
            model_name='xasuploadauxdata',
            name='aux_image',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='xasuploadauxdata',
            name='aux_thumbnail',
            field=models.TextField(blank=True),
        ),
    ]