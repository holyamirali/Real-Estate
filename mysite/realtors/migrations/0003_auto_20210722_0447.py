# Generated by Django 3.2.4 on 2021-07-22 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0002_realtor_photo_main'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='email',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='realtor',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='realtor',
            name='phone',
            field=models.CharField(max_length=15),
        ),
    ]
