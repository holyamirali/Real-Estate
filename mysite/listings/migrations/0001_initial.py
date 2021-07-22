# Generated by Django 3.2.4 on 2021-07-06 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='listings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(blank=True, max_length=25)),
                ('property_id', models.CharField(blank=True, max_length=30)),
                ('type', models.CharField(blank=True, max_length=15)),
                ('address', models.TextField(blank=True)),
                ('bathroom', models.CharField(blank=True, max_length=5)),
                ('bedroom', models.CharField(blank=True, max_length=5)),
                ('infrastructure', models.CharField(blank=True, max_length=15)),
                ('details', models.TextField(blank=True)),
            ],
        ),
    ]
