# Generated by Django 4.2.2 on 2023-06-16 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_booking_trip_end_alter_booking_trip_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='brand',
            field=models.CharField(default='', max_length=100),
        ),
    ]
