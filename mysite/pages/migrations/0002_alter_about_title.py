# Generated by Django 3.2.4 on 2021-07-22 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]