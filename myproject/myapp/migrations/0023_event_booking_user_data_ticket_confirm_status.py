# Generated by Django 4.1.5 on 2023-01-24 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0022_event_booking_user_data_event_booking_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='event_booking_user_data',
            name='ticket_confirm_status',
            field=models.BooleanField(default=False),
        ),
    ]
