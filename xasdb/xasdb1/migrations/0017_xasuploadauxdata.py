# Generated by Django 2.0.5 on 2018-07-09 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('xasdb1', '0016_auto_20180622_1549'),
    ]

    operations = [
        migrations.CreateModel(
            name='XASUploadAuxData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aux_description', models.CharField(default='', max_length=256, verbose_name='Description')),
                ('aux_file', models.FileField(upload_to='uploads/%Y/%m/%d/')),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xasdb1.XASFile')),
            ],
        ),
    ]