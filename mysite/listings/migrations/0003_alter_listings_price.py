# Generated by Django 3.2.4 on 2021-07-22 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20210706_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]
