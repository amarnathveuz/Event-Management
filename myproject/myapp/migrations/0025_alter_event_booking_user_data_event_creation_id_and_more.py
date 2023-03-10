# Generated by Django 4.1.5 on 2023-01-24 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0024_event_booking_user_data_event_creation_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event_booking_user_data',
            name='event_creation_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Event_Booking_user_Data_event_id', to='myapp.event_booking_table'),
        ),
        migrations.AlterField(
            model_name='event_booking_user_data',
            name='event_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Event_Booking_user_Data_bookig_table_id', to='myapp.event_creation'),
        ),
    ]
