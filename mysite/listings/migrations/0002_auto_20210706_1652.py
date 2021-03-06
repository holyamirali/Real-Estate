# Generated by Django 3.2.4 on 2021-07-06 12:22

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0002_realtor_photo_main'),
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listings',
            name='property_id',
        ),
        migrations.RemoveField(
            model_name='listings',
            name='type',
        ),
        migrations.AddField(
            model_name='listings',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='listings',
            name='list_data',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='listings',
            name='photo_1',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='listings',
            name='photo_2',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='listings',
            name='photo_main',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='listings',
            name='realtor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='realtors.realtor'),
        ),
        migrations.AddField(
            model_name='listings',
            name='title',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='listings',
            name='bathroom',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='listings',
            name='bedroom',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='listings',
            name='details',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='listings',
            name='infrastructure',
            field=models.CharField(max_length=100),
        ),
    ]
